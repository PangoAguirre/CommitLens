import subprocess

class gitCommitExtractor:

    def __init__(self):
        pass

    def extract_allcommits(self, name, destination_directory):
        repo_path = f"{destination_directory}/{name}"
        subprocess.run(["cd", repo_path])
        subprocess.run(["git", "log", "--all", "--pretty=format:'COMMIT|%H|%an|%ae|%aI|%s|%P'", 
                        "--numstat", ">", f"{destination_directory}/commits_{name}.txt"])
        