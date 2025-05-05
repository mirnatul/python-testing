import random

print(random.randrange(1, 10))  # 1 to 9


age = 20
balance = 15.555
a = f"My name is John, I am {age} years old"
b = f"Balance is, {balance:.2f}"  # show up to 2 decimal

abc = "Hello there I am using whatsapp"
print("there" in abc)
print("there" not in abc)

sli = abc[2:5]
sli_start = abc[:5]
sli_end = abc[2:]
sli_negative = abc[-5:-2]  # last character is indexed -1
print(sli, sli_start, sli_end, sli_negative)
