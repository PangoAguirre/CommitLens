class CommitRepository:
    def __init__(self, db_client):
        self.db_client = db_client

    def add_commit(self, commit_hash, repo_id, author_id, commit_date, message):
        cursor = self.db_client.connection.cursor()
        query = """
        INSERT INTO commits (commit_hash, repo_id, author_id, commit_date, message)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (commit_hash) DO NOTHING
        """
        cursor.execute(query, (commit_hash, repo_id, author_id, commit_date, message))
        self.db_client.connection.commit()
        cursor.close()

    def get_commit_by_id(self, commit_id):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM commits WHERE id = %s"
        cursor.execute(query, (commit_id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_commit_by_hash(self, commit_hash):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM commits WHERE commit_hash = %s"
        cursor.execute(query, (commit_hash,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_all_commits(self):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM commits"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def delete_commit(self, commit_id):
        cursor = self.db_client.connection.cursor()
        query = "DELETE FROM commits WHERE id = %s"
        cursor.execute(query, (commit_id,))
        self.db_client.connection.commit()
        cursor.close()

    def update_commit(self, commit_id, new_commit_hash, new_repo_id, new_author_id, new_commit_date, new_message):
        cursor = self.db_client.connection.cursor()
        query = """
        UPDATE commits
        SET commit_hash = %s, repo_id = %s, author_id = %s, commit_date = %s, message = %s
        WHERE id = %s
        """
        cursor.execute(query, (new_commit_hash, new_repo_id, new_author_id, new_commit_date, new_message, commit_id))
        self.db_client.connection.commit()
        cursor.close()

    def get_commits_by_author(self, author_id):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM commits WHERE author_id = %s"
        cursor.execute(query, (author_id,))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_commits_by_repo(self, repo_id):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM commits WHERE repo_id = %s"
        cursor.execute(query, (repo_id,))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_commits_by_date_range(self, start_date, end_date):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM commits WHERE commit_date BETWEEN %s AND %s"
        cursor.execute(query, (start_date, end_date))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_commit_count_by_author(self, author_id):
        cursor = self.db_client.connection.cursor()
        query = "SELECT COUNT(*) FROM commits WHERE author_id = %s"
        cursor.execute(query, (author_id,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0
    
    def get_commit_count_by_repo(self, repo_id):
        cursor = self.db_client.connection.cursor()
        query = "SELECT COUNT(*) FROM commits WHERE repo_id = %s"
        cursor.execute(query, (repo_id,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0
    
    def get_commit_count_by_date_range(self, start_date, end_date):
        cursor = self.db_client.connection.cursor()
        query = "SELECT COUNT(*) FROM commits WHERE commit_date BETWEEN %s AND %s"
        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0
    
    def get_commit_count_by_author_and_repo(self, author_id, repo_id):
        cursor = self.db_client.connection.cursor()
        query = "SELECT COUNT(*) FROM commits WHERE author_id = %s AND repo_id = %s"
        cursor.execute(query, (author_id, repo_id))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0
    
    def get_commit_count_by_author_and_date_range(self, author_id, start_date, end_date):
        cursor = self.db_client.connection.cursor()
        query = "SELECT COUNT(*) FROM commits WHERE author_id = %s AND commit_date BETWEEN %s AND %s"
        cursor.execute(query, (author_id, start_date, end_date))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0
    
    def get_commit_count_by_repo_and_date_range(self, repo_id, start_date, end_date):
        cursor = self.db_client.connection.cursor()
        query = "SELECT COUNT(*) FROM commits WHERE repo_id = %s AND commit_date BETWEEN %s AND %s"
        cursor.execute(query, (repo_id, start_date, end_date))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0
    
    def get_commit_count_by_author_repo_and_date_range(self, author_id, repo_id, start_date, end_date):
        cursor = self.db_client.connection.cursor()
        query = "SELECT COUNT(*) FROM commits WHERE author_id = %s AND repo_id = %s AND commit_date BETWEEN %s AND %s"
        cursor.execute(query, (author_id, repo_id, start_date, end_date))
        result = cursor.fetchone()
        cursor.close()
        return result[0] if result else 0
    