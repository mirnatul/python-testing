my_set = {"apple", "banana", "cherry"}
my_set.add("pineapple")

# print(my_set)

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 4}
set3 = {8, 9, 4}

# # union
# set4 = set1.union(set2)
# set5 = set1.union(set2, set3)
# set6 = set1 | set2 | set3

# # update
# set1.update(set3)
# set1.update(set3, set2)


# # intersection
# set4 = set1.intersection(set2)
# set5 = set1.intersection(set2, set3)
# set6 = set1 & set2 & set3

# # intersection_update
# set1.intersection_update(set3)
# set1.intersection_update(set3, set2)

# # difference
# set4 = set1.difference(set2)
# set5 = set1.difference(set2, set3)
# set6 = set1 - set2 - set3

# # difference_update
# set1.intersection_update(set3)
# set1.intersection_update(set3, set2)

# difference
set4 = set1.symmetric_difference(set2)
set5 = set1.symmetric_difference(set2, set3)
set6 = set1 ^ set2 ^ set3

# difference_update
set1.symmetric_difference_update(set3)
set1.symmetric_difference_update(set3, set2)
print(set1)
