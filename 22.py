import json

entegal = open("states.json")
data = json.load(entegal)
state_names = []

for i in data["states"]:
    f1 = {'name': i["name"]}
    state_names.append(f1)
output = '\n'.join([f"[state : {state_name['name']}]" for state_name in state_names])
print(output)
