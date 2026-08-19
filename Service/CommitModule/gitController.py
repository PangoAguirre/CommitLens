import Repo, Client, commitExtractor

class gitController:
    def __init__(self, nameUser, emailUser):
        self.destination_directory = "API_Service/CloneRepository"
        self.client = Client.gitClient(nameUser, emailUser)
        self.repo = Repo.gitRepo()
        self.commitExtractor = commitExtractor.gitCommitExtractor()

    def clone_repository(self, repository_url):
        self.client.clone_repository(repository_url, self.destination_directory)

    def delete_repository(self, repository_url):
        self.client.delete_repository(repository_url, self.destination_directory)

    def get_infoRepo(self, repository_url):
        return self.repo.get_info(repository_url, self.destination_directory)
    
    def extract_allcommits(self, name):
        return self.commitExtractor.extract_allcommits(name, self.destination_directory)