import json

entegal = open("payments.json")
data = json.load(entegal)
state_names = []

for i in data["employees"]:
    f1 = {'name': i["name"], 'job_title': i["job_title"]}
    state_names.append(f1)

output = '\n'.join([f"{employee['name']} ({employee['job_title']})" for employee in state_names])
print(output)