x = lambda a: a + 10
print(x(5))  # 15
# another example
y = lambda a, b: a * b


def fun1(n):
    return lambda a: a * n


# here double is also a function - lambda a: a * 2
double = fun1(2)
# here triple is also a function - lambda a: a * 3
triple = fun1(3)

print(double(11))  # 22
print(triple(11))  # 33
