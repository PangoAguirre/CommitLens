from API_Service.RepositoryModule import dbClient

class Database:
    def __init__(self, host, database, user, password):
        self.connection = dbClient(host, database, user, password).connection
        self.cursor = self.connection.cursor()

        self.initCommitTable = """
        CREATE TABLE IF NOT EXISTS commits (
            id SERIAL PRIMARY KEY,
            commit_hash VARCHAR(40) NOT NULL,
            repo_id INTEGER REFERENCES repositories(id),
            author_id VARCHAR(40) NOT NULL,
            commit_date TIMESTAMP NOT NULL,
            message TEXT NOT NULL,
            UNIQUE(commit_hash)"""
        
        self.initAuthorTable = """
        CREATE TABLE IF NOT EXISTS authors (
            id SERIAL PRIMARY KEY,
            author_name VARCHAR(100) NOT NULL,
            author_email VARCHAR(100) NOT NULL,
            UNIQUE(author_name, author_email)"""
        
        self.RepoTable = """
        CREATE TABLE IF NOT EXISTS repositories (
            id SERIAL PRIMARY KEY,
            repo_name VARCHAR(100) NOT NULL,
            repo_owner VARCHAR(100) NOT NULL,
            repo_url VARCHAR(200) NOT NULL,
            repo_default_branch VARCHAR(100) NOT NULL,
            repo_created_at TIMESTAMP NOT NULL,
            repo_updated_at TIMESTAMP NOT NULL,
            UNIQUE(repo_name, repo_url)"""
        
        self.FilesChangesTable = """
        CREATE TABLE IF NOT EXISTS file_changes (
            id SERIAL PRIMARY KEY,
            commit_id INTEGER REFERENCES commits(id),
            file_path VARCHAR(200) NOT NULL,
            status VARCHAR(10),
            added_lines INTEGER,
            deleted_lines INTEGER,
            UNIQUE(commit_id, file_path)"""
    
        self.UserTable = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            UNIQUE(username, email)"""

        return self.cursor, self.connection

    def initialize(self):
        self.cursor.execute(self.initCommitTable)
        self.cursor.execute(self.initAuthorTable)
        self.cursor.execute(self.RepoTable)
        self.cursor.execute(self.FilesChangesTable)
        self.cursor.execute(self.UserTable)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()