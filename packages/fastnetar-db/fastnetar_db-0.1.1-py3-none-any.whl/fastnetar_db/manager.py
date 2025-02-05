from fastnetar_db.database import Database

databases = {}
def add_database(database : Database):
    databases[database.db_url] = database

def get_default_database():
    return databases[0]