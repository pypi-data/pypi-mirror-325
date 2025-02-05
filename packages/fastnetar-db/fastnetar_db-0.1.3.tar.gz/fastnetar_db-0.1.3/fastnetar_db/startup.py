from fastnetar_db.database import databases
async def startup():
    for database_url in databases:
        db = databases[database_url]
        await db.sync_database()