import subprocess

class gitCommitExtractor:

    def __init__(self):
        self.datosCommit = [["commit_sha", "author_name", "author_email", "author_date", "commit_message", "parent_sha"]]
        self.datosFiles = [["commit_sha", "file_name", "insertions", "deletions"]]

    def extract_allcommits(self, name, destination_directory):
        result = subprocess.run(["git", "log", "--all", "--pretty=format:'COMMIT|%H|%an|%ae|%aI|%s|%P'", 
                        "--numstat"], capture_output=True, text=True, cwd=f"{destination_directory}/{name}")
        
        self.clean_data(result)

        return [self.datosCommit, self.datosFiles]

    def clean_data(self, result):
        for linea in result.stdout.splitlines():
            if linea.startswith("'COMMIT"):
                commit_sha = linea.split("|")[1]
                author_name = linea.split("|")[2]
                author_email = linea.split("|")[3]
                author_date = linea.split("|")[4]
                commit_message = linea.split("|")[5]
                parent_sha = linea.split("|")[6] if len(linea.split("|")) > 6 else ""
                self.datosCommit.append([commit_sha, author_name, author_email, author_date, commit_message, parent_sha])
            elif linea.strip():
                file_stats = linea.split("\t")
                if len(file_stats) == 3:
                    insertions = file_stats[0]
                    deletions = file_stats[1]
                    file_name = file_stats[2]
                    self.datosFiles.append([commit_sha, file_name, insertions, deletions])