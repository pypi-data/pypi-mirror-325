from fastnetar_db.database import databases
async def startup():
    for database in databases:
        await database.sync_database()