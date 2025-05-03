# parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # also Person.__init__ ...
        self.graduationyear = year

    def welcome(self):
        print(
            f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}"
        )


y = Student("Mike", "Olsen", 2019)
y.printname()
y.welcome()


x = Person("John", "Doe")
x.printname()
