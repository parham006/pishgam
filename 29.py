import xmltodict

data = open("payments.xml")
data_read = xmltodict.parse(data.read())
root = data_read["employees"]
root_2 = root["employee"]
lst = []

for i in root_2:
    if int(i["age"]) <= 30:
        lst.append(i)
output = '\n'.join([f"{employee['name']} ({employee['age']})" for employee in lst])
print(output)
