class Person:

    def __init__(self, name, age, job, birth_place):
        self.name = name
        self.age = age
        self.job = job
        self.birth_place = birth_place

    def __str__(self):
        return f"Hello\n I'm {self.name}and I'm {self.age} and I'm {self.job} and I'm from {self.birth_place}"


information = Person("Sirous", "23", "Unemployed", "Zabol")
print(information)
