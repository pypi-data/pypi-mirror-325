from libsql_client import create_client, Client
from passlib.context import CryptContext



class TableSchema:
    """Class-based approach for defining database tables and applying schema changes."""

    def __init__(self, name, columns, constraints=None):
        """
        Initialize a table schema.

        Args:
            name (str): The table name.
            columns (dict): Column definitions, e.g., {"id": "INTEGER PRIMARY KEY AUTOINCREMENT"}.
            constraints (list, optional): Additional SQL constraints like UNIQUE, FOREIGN KEY.
        """
        self.name = name
        self.columns = columns  # Dictionary: {column_name: column_definition}
        self.constraints = constraints or [] # Allow additional constraints (e.g., UNIQUE, FOREIGN KEYS)

    async def create_table(self, client):
        """Create table with dynamic constraints."""

        # Define columns
        column_defs = [f"{col} {definition}" for col, definition in self.columns.items()]
        
        # Append constraints (if any)
        if self.constraints:
            column_defs.extend(self.constraints)

        query = f"CREATE TABLE IF NOT EXISTS {self.name} ({', '.join(column_defs)});"
        
        await client.execute(query)

        print(f"\t✅ Table '{self.name}' is up-to-date.")

    async def alter_table(self, client):
        """Alter table by adding missing columns dynamically."""
        result = await client.execute(f"PRAGMA table_info({self.name})")
        existing_columns = {row[1] for row in result.rows}  # Extract column names

        for col_name, col_def in self.columns.items():
            if col_name not in existing_columns:
                # Remove DEFAULT CURRENT_TIMESTAMP for SQLite compatibility
                col_def = col_def.replace("DEFAULT CURRENT_TIMESTAMP", "").strip()
                await client.execute(f"ALTER TABLE {self.name} ADD COLUMN {col_name} {col_def};")
                print(f"\t✅ Column '{col_name}' added to '{self.name}' table.")
                
                # If adding 'created_at', set a default manually
                if col_name == "created_at":
                    await client.execute(f"UPDATE {self.name} SET {col_name} = CURRENT_TIMESTAMP WHERE {col_name} IS NULL;")

    async def sync_table(self,client):
        """Ensure the table exists and all necessary columns are added."""
        await self.create_table(client)
        await self.alter_table(client)

class Database:
    def __init__(self, db_url : str,admin_username : str,admin_password : str, tables : list[TableSchema]):
        self.db_url = db_url
        self.client : Client = create_client(db_url)
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.tables = tables
        self.password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def sync_database(self):
        """Ensure all tables and schema updates are applied."""
        print("🔄 Syncing database schema...")
        for table in self.tables:
            await table.sync_table(self.client)

        # Ensure an admin user exists
        existing_admin = await self.client.execute("SELECT id FROM users WHERE username = ?", (self.admin_username,))
        if not existing_admin.rows:
            hashed_password = self.password_context.hash(self.admin_password)
            await self.client.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'admin')",
                            (self.admin_username, hashed_password))
            print("\t✅ Admin user created successfully!")
        else:
            print("\t✅ Admin user already exists!")

        print("\t✅ Database schema is fully synced!")

        return "Database synced successfully!"