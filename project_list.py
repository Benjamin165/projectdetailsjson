import json
import project
class ProjectList:
    def __init__(self):
        with open("projects.txt", "r") as read_file:
            self.data = json.load(read_file)

    def add_project(self, project):
        last_id = self.data["data"][-1]["monument_id"]
        self.data["data"].append(project.converted_project())
        self.data["data"][-1]["monument_id"] = last_id + 1



#for testing 
p = project.Project(100, 4, "Amazin")
print(p.converted_project())
x = ProjectList()
print(x.data["data"][7])
x.add_project(p)
print()
