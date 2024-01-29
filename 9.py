from time import sleep

class Car:
    def __init__(self, name, model, acceleration, speed, engine_speed):
        self.name = name
        self.model = model
        self.acceleration = acceleration
        self.speed = speed
        self.engine_speed = engine_speed

    def __str__(self):
        return f"({self.name} {self.model})"

    def ratioo_supra(self):
        time = self.acceleration
        speed = self.speed
        while speed <= 260:
            engine_speed = 1 + (speed // 50)
            ratio = speed, time, engine_speed
            print(f"\r mph {ratio}", end="", flush=True)
            speed += 20
            time += 1
            sleep(0.5)

    def ratioo_gtr(self):
        time = self.acceleration
        speed = self.speed
        while speed <= 315:
            engine_speed = 1 + (speed // 50)
            ratio = speed, time, engine_speed
            print(f"\r mph {ratio}", end="", flush=True)
            speed += 25
            time += 0.7
            sleep(0.5)

mk4 = Car("Toyota Supra", "MK4", 0, 0, 1)
gtr = Car("Nissan", "GTR", 0, 0, 1)

while True:
    try:
        user_input = input("Which car information do you want? (mk4/gtr): ")
        if user_input == "mk4":
            mk4.ratioo_supra()
        elif user_input == "gtr":
            gtr.ratioo_gtr()
        else:
            raise ValueError
        break
    except ValueError:
        print("Invalid choice. Please enter 'mk4' or 'gtr'.")