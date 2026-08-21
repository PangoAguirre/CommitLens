import psycopg2

class dbClient:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

    def get_cursor(self):
        return self.connection.cursor()