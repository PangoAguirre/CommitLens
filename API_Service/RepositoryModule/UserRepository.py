class UserRepository:
    def __init__(self, db_client):
        self.db_client = db_client

    def add_user(self, username, email):
        cursor = self.db_client.connection.cursor()
        query = """
        INSERT INTO users (username, email)
        VALUES (%s, %s)
        ON CONFLICT (username, email) DO NOTHING
        """
        cursor.execute(query, (username, email))
        self.db_client.connection.commit()
        cursor.close()

    def get_user_by_id(self, user_id):
        cursor = self.db_client.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def get_user_by_username(self, username):
        cursor = self.db_client.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        return user
    
    def get_all_users(self):
        cursor = self.db_client.connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        return users

    def delete_user(self, user_id):
        cursor = self.db_client.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.db_client.connection.commit()
        cursor.close()

    def update_user(self, user_id, new_username, new_email):
        cursor = self.db_client.connection.cursor()
        query = """
        UPDATE users
        SET username = %s, email = %s
        WHERE id = %s
        """
        cursor.execute(query, (new_username, new_email, user_id))
        self.db_client.connection.commit()
        cursor.close()

    def get_users_by_email_domain(self, domain):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM users WHERE email LIKE %s"
        cursor.execute(query, (f"%@{domain}",))
        users = cursor.fetchall()
        cursor.close()
        return users