import json

entegal = open("states.json")
data = json.load(entegal)
state_names = []

for i in data["states"]:
    f1 = {'state_name': i["name"]}
    state_names.append(f1)

f2 =open("new_state.json","w")
json.dump(state_names, f2)
print("done")