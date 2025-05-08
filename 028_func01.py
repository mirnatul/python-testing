def my_func(name):  # name is parameter
    print("Hello, ", name)


my_func("John")  # John is argument


def func(name2, name1):
    print("Hello", name1, name2)


func(name1="John", name2="Doe")


def my_function(**kid):
    print("His last name is", kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# if there is no country name we will consider Norway
def country_name(country="Norway"):
    pass
