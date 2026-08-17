import subprocess

from API_Service.CommitModule import gitClient, gitRepoInfo

class gitController:
    def __init__(self, nameUser, emailUser):
        self.destination_directory = "./API_Service/CloneRepository"
        self.git_client = gitClient(nameUser, emailUser)
        self.gitRepoInfo = gitRepoInfo()

    def clone_repository(self, repository_url):
        self.git_client.clone_repository(repository_url, self.destination_directory)

    def get_infoRepo(self, repository_url):
        return self.gitRepoInfo.get_infoRepo(repository_url, self.destination_directory)
    
