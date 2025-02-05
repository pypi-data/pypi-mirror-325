from fastnetar_db.database import Database

def sync_database(database : Database):
    return database.sync_database()

startup : list[callable] = [
    sync_database
]