def avrage(*args):
    x = sum(args) / len(args)
    print(x)


mount = int(input("how many number you wanna add ? :"))
numbers = []
for i in range(mount):
    while True:
        try:
            number = int(input("Enter a number: "))
            numbers.append(number)
            break
        except ValueError:
            print("its not the number! try again")
avrage(*numbers)
