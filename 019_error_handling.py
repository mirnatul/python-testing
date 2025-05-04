def check_age(age):
    if not isinstance(age, int):
        raise TypeError("Only integers are allowed")
    if age < 0:
        raise Exception("Sorry, no numbers below zero")
    print(f"Age is valid: {age}")


try:
    check_age(-5)  # Will raise a general Exception
except Exception as e:
    print("Error:", e)

try:
    check_age("twenty")  # Will raise a TypeError
except Exception as e:
    print("Error:", e)

try:
    check_age(25)  # Valid input
except Exception as e:
    print("Error:", e)
