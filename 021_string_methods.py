abc = "Hello there I am using Whatsapp there"
# abc = ["Orange", "Apple", "Banana"]


a = abc.isupper()
# b = abc.endswith("Hello", 3)
# c = abc.endswith("Hello")
# d = abc.endswith(("Hello", "there"))
# b = abc.split(",")
# c = abc.split(",", 1)
print(a)
# print(b)
# print(c)
# print(d)

# isdecimal() ⊂ isdigit() ⊂ isnumeric()


def is_number(s):
    try:
        float(s)  # or int(s) if you want only integers
        return True
    except ValueError:
        return False
