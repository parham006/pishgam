from math import pi


class Rectangle:
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

    def perimeter(self):
        print((self.length + self.width) * 2)

    def area(self):
        print(self.length * self.width)


class Circle:
    def __init__(self, Radius):
        self.Radius = Radius

    def perimeter(self):
        print((self.Radius + Radius) * pi)

    def area(self):
        print((self.Radius * Radius) * pi)


while True:
    try:
        n = int(input("enter the length : "))
        m = int(input("enter the width : "))

        mostatil = Rectangle(n, m)
        dayere = Circle(n)

        x = input("Circle or Rectangle --> c/r : ")
        if x == "r":
            mostatil.area()
            mostatil.perimeter()
        elif x == "r":
            dayere.area()
            dayere.perimeter()
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
