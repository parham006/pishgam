import xmltodict

data = open("payments.xml")
data_read = xmltodict.parse(data.read())
root = data_read["employees"]
root_2 = root["employee"]
lst = []

for i in root_2:
    if i["job_title"] == "Python Developer":
        for j in i["monthly_payment"].values():
            lst.append(float(j))

avg = sum(lst) / len(lst)
print(int(avg),end=".0$")
