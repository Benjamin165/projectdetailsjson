import json
class project_list:
    def __init__(self):
        with open("projects.txt", "r") as read_file:
            self.data = json.load(read_file)
    def add_project(self, project):
        self.data["data"].append(project)

with open("projects.txt", "r") as read_file:
    data = json.load(read_file)

#for testing 
print(data["data"][0]["monument_id"])
