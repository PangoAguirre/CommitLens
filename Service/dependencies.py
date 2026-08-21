from Service.Shared import dbClient


db = dbClient()

def get_user_service():
    return UserService(UserRepository(db))