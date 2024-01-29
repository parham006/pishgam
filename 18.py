import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

backup = {"name": 'parham', "code": 1234, "job": 'software_eng'}
backup = tuple(backup.values())

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()


def save(record):
    command = f"INSERT INTO employees(name,code,job) VALUES {(record[0], record[1], record[2])};"
    cur.execute(command)


user = [i[1:] for i in records]
if backup in user:
    print("this file exist")
else:
    save(backup)
    print("it file saved")

for i in records:
    print(i)
    print(len(records), "exist")

con.commit()
con.close()
