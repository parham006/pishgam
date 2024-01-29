import jdatetime
def time(briths):
    now = int(jdatetime.datetime.now().year)
    data = now - briths
    print(data)
y = int(input("enter your jalali briths_y : "))
time(y)
