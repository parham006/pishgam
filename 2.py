from time import sleep
import random
import os
def send(poya):
    password = []
    for i in range(poya):
        ps = random.choice(range(0, 10))
        password.append(str(ps))
    password = "".join(password)
    return password
counter = 0
time_left = 60

print(send(6))
print("-" * 6)

while True:
    time_left -= 1
    sleep(1)
    print("\rTime Left:", time_left, end="", flush=True)

    if time_left == 0:
        os.system("cls")
        print("\r" + send(6))
        print("-" * 6)
        time_left = 6
