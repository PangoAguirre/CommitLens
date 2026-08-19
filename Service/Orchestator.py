import RepositoryModule, CommitModule, UserModule

class Orchestator:
    def __init__(self):
        self.dbController = RepositoryModule.Controller()
        self.userController = UserModule.UserController()
        self.commitController = CommitModule.gitController()

        