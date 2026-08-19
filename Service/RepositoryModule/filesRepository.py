class FilesRepository:
    def __init__(self, db_client):
        self.db_client = db_client

    def add_file(self, file_path, commit_id, status, added_lines, deleted_lines):
        cursor = self.db_client.connection.cursor()
        query = """
        INSERT INTO file_changes (file_path, commit_id, status, added_lines, deleted_lines)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (commit_id, file_path) DO NOTHING
        """
        cursor.execute(query, (file_path, commit_id, status, added_lines, deleted_lines))
        self.db_client.connection.commit()
        cursor.close()

    def get_file_by_id(self, file_id):
        cursor = self.db_client.connection.cursor()
        cursor.execute("SELECT * FROM files WHERE id = %s", (file_id,))
        file_record = cursor.fetchone()
        cursor.close()
        return file_record
    
    def get_files_by_commit(self, commit_id):
        cursor = self.db_client.connection.cursor()
        cursor.execute("SELECT * FROM file_changes WHERE commit_id = %s", (commit_id,))
        files = cursor.fetchall()
        cursor.close()
        return files
    
    def get_all_files(self):
        cursor = self.db_client.connection.cursor()
        cursor.execute("SELECT * FROM file_changes")
        files = cursor.fetchall()
        cursor.close()
        return files
    
    def delete_file(self, file_id):
        cursor = self.db_client.connection.cursor()
        cursor.execute("DELETE FROM file_changes WHERE id = %s", (file_id,))
        self.db_client.connection.commit()
        cursor.close()

    def update_file(self, file_id, new_file_path, new_commit_id, new_status, new_added_lines, new_deleted_lines):
        cursor = self.db_client.connection.cursor()
        query = """
        UPDATE file_changes
        SET file_path = %s, commit_id = %s, status = %s, added_lines = %s, deleted_lines = %s
        WHERE id = %s
        """
        cursor.execute(query, (new_file_path, new_commit_id, new_status, new_added_lines, new_deleted_lines, file_id))
        self.db_client.connection.commit()
        cursor.close()