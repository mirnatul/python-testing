class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 27")

for i in [car1, boat1]:
    i.move()
