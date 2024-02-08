import xmltodict

data = open("flights.xml")
data_read = xmltodict.parse(data.read())
root = data_read["flights"]
root_2 = root["flight"]
lst = []

for i in root_2:
    if i["destination"].lower() == "paris":
        lst.append(i)
print(lst)