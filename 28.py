import json

f1 = open("payments.json")
data = json.load(f1)
employees = {}

for emp in data["employees"]:
    salary = [i for i in emp["monthly_payment"].values()]
    ave = sum(salary) / len(salary)
    employees.setdefault(emp["name"], ave)
    soort =sorted(employees.items(), key=lambda x: x[1], reverse=True)
print(soort)
