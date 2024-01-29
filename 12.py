class Calculator:
    def __init__(self, first, action, second):
        self.first = first
        self.second = second
        self.action = action

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second

    def multiply(self):
        return self.first * self.second

    def divide(self):
        if self.second != 0:
            return self.first / self.second
        else:
            return "Cannot divide by zero"

def actions():
    while True:
        try:
            f_number = int(input("First Number: "))
            types = input("What action do you need (+ or - or * or /): ")
            s_number = int(input("Second Number: "))

            calculator = Calculator(f_number, types, s_number)

            if calculator.action == "+":
                print(calculator.add())
            elif calculator.action == "-":
                print(calculator.subtract())
            elif calculator.action == "*":
                print(calculator.multiply())
            elif calculator.action == "/":
                print(calculator.divide())
            else:
                print("Invalid action. Try again")
        except ValueError:
            print("Invalid input. Try again")

actions()
