class AuthorRepository:
    def __init__(self, db_cursor):
        self.cursor = db_cursor

    def add_author(self, author_name, author_email):
        try:
            self.cursor.execute(
                "INSERT INTO authors (author_name, author_email) VALUES (%s, %s) ON CONFLICT (author_name, author_email) DO NOTHING",
                (author_name, author_email)
            )
        except Exception as e:
            print(f"Error adding author: {e}")

    def get_author_id(self, author_name, author_email):
        try:
            self.cursor.execute(
                "SELECT id FROM authors WHERE author_name = %s AND author_email = %s",
                (author_name, author_email)
            )
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error retrieving author ID: {e}")
            return None
        
    def get_author_by_id(self, author_id):
        try:
            self.cursor.execute(
                "SELECT author_name, author_email FROM authors WHERE id = %s",
                (author_id,)
            )
            result = self.cursor.fetchone()
            return {"author_name": result[0], "author_email": result[1]} if result else None
        except Exception as e:
            print(f"Error retrieving author by ID: {e}")
            return None

    def get_all_authors(self):
        try:
            self.cursor.execute("SELECT id, author_name, author_email FROM authors")
            results = self.cursor.fetchall()
            return [{"id": row[0], "author_name": row[1], "author_email": row[2]} for row in results]
        except Exception as e:
            print(f"Error retrieving all authors: {e}")
            return []
        
    def delete_author(self, author_id):
        try:
            self.cursor.execute(
                "DELETE FROM authors WHERE id = %s",
                (author_id,)
            )
        except Exception as e:
            print(f"Error deleting author: {e}")

    def update_author(self, author_id, new_name, new_email):
        try:
            self.cursor.execute(
                "UPDATE authors SET author_name = %s, author_email = %s WHERE id = %s",
                (new_name, new_email, author_id)
            )
        except Exception as e:
            print(f"Error updating author: {e}")