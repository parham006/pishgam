import sqlite3

con = sqlite3.connect("info.ab")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customers(name,city,Pnumber);")
cur.execute("INSERT INTO customers VALUES('parham','tehran','09196885373');")
cur.execute("INSERT INTO customers VALUES('hossien','yazd','0919456373');")
cur.execute("INSERT INTO customers VALUES('ali','kerman','09196823373');")
cur.execute("SELECT * FROM customers")

records = cur.fetchall()
counter = 0
for i in records:
    counter +=1
    if counter == 4:
        break
    print(i)
con.commit()
con.close()
print("done")
