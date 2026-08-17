import subprocess

# Clase que maneja la clonación de repositorios Git.
class gitClient:
    def __init__(self, nameUser, emailUser):
        self.nameUser = nameUser
        self.emailUser = emailUser

    def clone_repository(self, repository_url, destination_directory):
        name = repository_url.split("/")[-1].replace(".git", "")
        subprocess.run(["git", "config", "--global", "user.name", self.nameUser])
        subprocess.run(["git", "config", "--global", "user.email", self.emailUser])
        subprocess.run(["mkdir", "-p", destination_directory + "/" + name])
        subprocess.run(["git", "clone", repository_url, destination_directory + "/" + name])