class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


car1 = Car("Ford", "Land Rover")
boat1 = Boat("Ibiza", "Touring 27")

for i in [car1, boat1]:
    i.move()
