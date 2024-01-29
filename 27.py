import json

f1 = open("payments.json")
data = json.load(f1)
employees = {}

for emp in data["employees"]:
    salary = [i for i in emp["monthly_payment"].values()]
    ave = sum(salary) / len(salary)
    employees.setdefault(emp["name"], ave)
most = max(employees.values())
most_salary =[i for i,j in employees.items() if j == most]
print(f"{most_salary} get highest salary :{most}")
