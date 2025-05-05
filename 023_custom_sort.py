def near_fifty(n):
    return abs(n - 50)


my_list = [100, 50, 65, 82, 23]
my_list.sort(key=near_fifty)
# print(my_list)  # [50, 65, 23, 82, 100]


# sort by case insensitive
a_list = ["banana", "Orange", "Kiwi", "cherry"]
a_list.sort(key=str.lower)
print(a_list)


# alternative way
b_list = ["banana", "Orange", "Kiwi", "cherry"]


def case(s):
    return s.lower()


b_list.sort(key=case)
print(b_list)
b_list.reverse()
