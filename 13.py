class human:
    def __init__(self, family_name, mager, job, ):
        self.mager = mager
        self.job = job
        self.family_name = family_name

    def speak(self):
        print(f" hello\n I'm mr.{self.family_name}\n I study {self.mager} and my job is {self.job} ")


class student(human):
    def __init__(self, family_name, mager, job, city):
        super().__init__(famil_yname, mager, job)
        self.city = city

    def speak(self):
        print(
            f" hello\n I'm ms.{self.family_name} I study {self.mager}\n my job is {self.job} and i born in {self.city}")

        H = human("rezaie", "sience", "dentis")
        S = student("hosseini", "math", "programmer", "tehran")
        user = input("Who do you want to meet? : ms.rezaie or mr.hossaini   ")
        if user == 'ms.rezaie':
            H.speak()
        elif user.lower() == "mr. hosseini":
            S.speak()
        else:
            print("Invalid input. Ms. Rezaie or Mr. Hosseini.")

