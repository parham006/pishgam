import sqlite3

con = sqlite3.connect("info.db.py")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers(name,city,average);")
cur.execute("INSERT INTO customers VALUES('parham','tehran','17.5');")
cur.execute("INSERT INTO customers VALUES('hossien','yazd','19.2');")
cur.execute("INSERT INTO customers VALUES('ali','kerman','15.23');")
cur.execute("INSERT INTO customers VALUES('hasan','karaj','16.77');")
cur.execute("SELECT * FROM customers")
counter = 0
records = cur.fetchall()
for i in records:
    average = float(i[2])
    if average >= 17:
        counter += 1
        print(i)
        if counter == 2:
            break
