import subprocess

class gitRepo:

    def __init__(self):
        pass

    def get_info(self, repository_url, destination_directory):
        info = []
        name = self.get_nameRepo(repository_url)
        owner = self.get_ownerRepo(repository_url)
        default_branch = self.get_defaultBranch(name, destination_directory)
        creation_date = self.get_infoCreationRepo(name, destination_directory)
        last_update_date = self.get_infoLastUpdateRepo(name, destination_directory)
        info.append(name)
        info.append(owner)
        info.append(default_branch) 
        info.append(creation_date)
        info.append(last_update_date)
        return info

    def get_nameRepo(self, repository_url):
        return repository_url.split("/")[-1].replace(".git", "")
    
    def get_ownerRepo(self, repository_url):
        return repository_url.split("/")[-2]
    
    def get_defaultBranch(self, name, destination_directory):
        repo_path = f"{destination_directory}/{name}"
        result = subprocess.run(["git", "-C", repo_path, "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
        
    def get_infoCreationRepo(self, name, destination_directory):
        repo_path = f"{destination_directory}/{name}"
        result = subprocess.run(["git", "-C", repo_path, "log", "--reverse", "--pretty=format:%ci"], capture_output=True, text=True)
        if result.returncode == 0:
            creation_date = result.stdout.splitlines()[0] if result.stdout else None
            return creation_date
        else:
            return None
        
    def get_infoLastUpdateRepo(self, name, destination_directory):
        repo_path = f"{destination_directory}/{name}"
        result = subprocess.run(["git", "-C", repo_path, "log", "-1", "--pretty=format:%ci"], capture_output=True, text=True)
        if result.returncode == 0:
            last_update_date = result.stdout.strip() if result.stdout else None
            return last_update_date
        else:
            return None