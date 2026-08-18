class RepoRepository:
    def __init__(self, db_client):
        self.db_client = db_client

    def add_repo(self, repo_name, repo_url):
        cursor = self.db_client.connection.cursor()
        query = """
        INSERT INTO repositories (repo_name, repo_url)
        VALUES (%s, %s)
        ON CONFLICT (repo_name, repo_url) DO NOTHING
        """
        cursor.execute(query, (repo_name, repo_url))
        self.db_client.connection.commit()
        cursor.close()

    def get_repo_by_id(self, repo_id):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM repositories WHERE id = %s"
        cursor.execute(query, (repo_id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_repo_by_name(self, repo_name):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM repositories WHERE repo_name = %s"
        cursor.execute(query, (repo_name,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_all_repos(self):
        cursor = self.db_client.connection.cursor()
        query = "SELECT * FROM repositories"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def delete_repo(self, repo_id):
        cursor = self.db_client.connection.cursor()
        query = "DELETE FROM repositories WHERE id = %s"
        cursor.execute(query, (repo_id,))
        self.db_client.connection.commit()
        cursor.close()

    def update_repo(self, repo_id, new_repo_name, new_repo_url):
        cursor = self.db_client.connection.cursor()
        query = """
        UPDATE repositories
        SET repo_name = %s, repo_url = %s
        WHERE id = %s
        """
        cursor.execute(query, (new_repo_name, new_repo_url, repo_id))
        self.db_client.connection.commit()
        cursor.close()

    def get_repos_by_author(self, author_id):
        cursor = self.db_client.connection.cursor()
        query = """
        SELECT DISTINCT r.*
        FROM repositories r
        JOIN commits c ON r.id = c.repo_id
        WHERE c.author_id = %s
        """
        cursor.execute(query, (author_id,))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_repos_by_commit(self, commit_id):
        cursor = self.db_client.connection.cursor()
        query = """
        SELECT r.*
        FROM repositories r
        JOIN commits c ON r.id = c.repo_id
        WHERE c.id = %s
        """
        cursor.execute(query, (commit_id,))
        results = cursor.fetchall()
        cursor.close()
        return results
    
    def get_repos_by_file(self, file_id):
        cursor = self.db_client.connection.cursor()
        query = """
        SELECT DISTINCT r.*
        FROM repositories r
        JOIN commits c ON r.id = c.repo_id
        JOIN file_changes f ON c.id = f.commit_id
        WHERE f.id = %s
        """
        cursor.execute(query, (file_id,))
        results = cursor.fetchall()
        cursor.close()
        return results