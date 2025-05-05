a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# if we just want to print
[print(i) for i in a]

# loop
abc = [i for i in a]

# loop with if
newL = [i - 1 for i in a if i % 2 == 0]

# loop with if and else
ano = [i - 1 if i % 2 == 0 else i + 10 for i in a]
