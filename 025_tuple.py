my_tuple = ("apple", "banana", "cherry")
x, y, z = my_tuple
x, *y = my_tuple
print(y)
# 1 item tuple (must have , or it will be a string)
# one_tuple = ("orange",)

# tuple to list
# my_tuple = list(my_tuple)
# (do the operation)
# list to tuple
# my_tuple = tuple(my_tuple)

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
a, *b = fruits  # b = ['banana', 'cherry']

print(b)


my_list = [1, 2, 3]
new_list = my_list * 2

list1 = [1, 2, 3]
list2 = [4, 5]
list1 += list2
