my_dict = {
    "brand": "Ford",
    "model": {"hello": "there", "I": "am", "using": "Whatsapp"},
    "year": 1964,
}

other_dict = my_dict.copy()
other_dict = dict(my_dict)

for key, value in my_dict.items():
    print(key, ": ", my_dict[key])
    if isinstance(value, dict):
        for y in value:
            print(y, ": ", value[y])


# items = my_dict.items()

# print(items)

# both removed pair, give error if key not found
# my_dict.pop("model")  # return value
# del my_dict["model"]  # don't return

# my_dict.clear()
# print(my_dict)

# del my_dict

keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}

item = my_dict.popitem()


my_dict = {"a": 1}
value = my_dict.setdefault("b", 100)
print(value)  # 100
print(my_dict)  # {'a': 1, 'b': 100}
