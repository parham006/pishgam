import time


def zaman(func):
    def wrapper(*args, **kwargs):
        y1 = time.time()
        func(*args, **kwargs)
        y2 = time.time()
        Yt = y1 - y2
        print(f"Function {func.__name__} took {Yt} second to execute")
        print("'" * 100)

    return wrapper


@zaman
def solution1(n):
    a = 0
    b = 1
    fib_list = [a]
    for i in range(n):
        a, b = b, a + b
        fib_list.append(a)


@zaman
def solution2(n):
    c = 0
    a = 0
    b = 1
    fib_list = [a]
    while c < n:
        a, b = b, a + b
        c += 1
        fib_list.append(a)


while True:
    try:
        x = int(input("Enter the number of terms: "))
        print("'" * 100)
        solution1(x)
        solution2(x)
        choice = input("Do you want to try again? (yes/no): ")
        if choice.lower() == "no":
            print("thanks", "\U0001F609")
            break
        elif choice.lower() != "yes":
            print("Invalid choice. Please enter 'yes' or 'no'.")
    except ValueError:
        print("Invalid input. Please enter a number.")
