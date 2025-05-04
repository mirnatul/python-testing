a, b = 5, 5

if a > b:
    print("Hello there")

print("a >") if a > b else print("a > or =")

print("a>") if a > b else print("=") if a == b else print("a > or =")
