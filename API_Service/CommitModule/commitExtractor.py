import subprocess

class gitCommitExtractor:

    def __init__(self):
        pass

    def extract_allcommits(self, name, destination_directory):
        with open(f"{destination_directory}/commits_{name}.txt", "w") as file:
            subprocess.run(["git", "log", "--all", "--pretty=format:'COMMIT|%H|%an|%ae|%aI|%s|%P'", 
                        "--numstat"], stdout=file)
        
        