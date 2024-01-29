import json

entegal = open("states.json")
data = json.load(entegal)
selected = []

for i in data["states"]:
    if i["name"].lower() in ["alaska", "new york", "florida"]:
        selected.append(i)

f2 =open("especials_states.json","w")
json.dump(selected, f2)
print("done")
