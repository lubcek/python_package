import os
from git import Repo

class ProjectNameCommand:
    def __init__(self):
        self.project = None

    def project_name(self):
        readme_files = ['README.md', 'README']
        try:
            for file_name in readme_files:
                if os.path.isfile(file_name):
                    with open(file_name, 'r') as file:
                        first_line = file.readline().strip()
                        if first_line:
                            if file_name.endswith('.md'):
                                first_line = first_line.lstrip('#')
                                first_line = first_line.strip('')
                                self.project = first_line
                                return
        except:
            try:
                repo = Repo(search_parent_directories=True)
                self.project = os.path.basename(repo.working_tree_dir)
            except:
                self.project = os.path.basename(os.getcwd())

    def execute(self):
        self.project_name()
        print(self.project)
