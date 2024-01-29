import random

def irancell():
    pn = ""
    lst = random.choice(["0939", "0936", "0933"])
    for i in range(7):
        pn += str(random.choice(range(0,9)))
    pn = f"{lst}{pn}"
    return pn
def hmrh_aval():
    pn = ""
    lst = random.choice(["0912", "0919", "0993"])
    for i in range(7):
        pn += str(random.choice(range(0,9)))
    pn = f"{lst}{pn}"
    return pn
print("Choose 'irancell' or 'hmrh_aval':")
user_input = input()
if user_input == "irancell":
    generated_number = irancell()
    print(generated_number)
elif user_input == "hmrh_aval":
    generated_number = hmrh_aval()
    print(generated_number)

