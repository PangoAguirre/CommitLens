from API_Service.RepositoryModule import AuthorRepository, CommitRepository, RepoRepository, UserRepository
from API_Service.RepositoryModule.filesRepository import FilesRepository


class Controller:
    def __init__(self):
        self.AuthorRepository = AuthorRepository()
        self.CommitRepository = CommitRepository()
        self.FilesRepository = FilesRepository()
        self.RepoRepository = RepoRepository()
        self.UserRepository = UserRepository()
