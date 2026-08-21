from Shared.dbClient import dbClient

def startup():
    db = dbClient()
    cursor = db.get_cursor()