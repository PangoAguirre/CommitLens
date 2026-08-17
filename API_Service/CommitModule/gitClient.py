import subprocess

class gitClient:
    def __init__(self, nameUser, emailUser):
        self.nameUser = nameUser
        self.emailUser = emailUser
        self.destination_directory = "./API_Service/CloneRepository"

    def clone_repository(self, repository_url, name):
        subprocess.run(["git", "config", "--global", "user.name", self.nameUser])
        subprocess.run(["git", "config", "--global", "user.email", self.emailUser])
        subprocess.run(["mkdir", "-p", self.destination_directory + "/" + name])
        subprocess.run(["git", "clone", repository_url, self.destination_directory + "/" + name])