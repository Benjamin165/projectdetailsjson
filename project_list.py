import json
import project
class ProjectList:
    def __init__(self):
        with open("projects.txt", "r") as read_file:
            self.data = json.load(read_file)

    def add_project(self, project):
        last_id = self.data["data"][-1]["monument_id"]
        self.data["data"].append(project.converted_project())
        new_last = last_id + 1
        self.data["data"][-1]["monument_id"] = new_last
        project.project_details["data"]["monument_id"] = new_last
        for x in range(project.amount_pics):
            project.pics["data"][x]["monument_id"] = new_last
        project.create_txt_file()
        projects_file = open("projects.txt", "w")
        projects_file.write(json.dumps(self.data))
        projects_file.close()
        

#for testing 
p = project.Project(4, "Amazin")
print(p.converted_project())
x = ProjectList()
print(x.data["data"][-1])
x.add_project(p)
print(x.data["data"][-1])