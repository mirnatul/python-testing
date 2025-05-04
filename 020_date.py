import datetime

x = datetime.datetime.now()
print(x)  # 2025-05-04 15:47:37.496397

# create datetime
y = datetime.datetime(2025, 2, 12)
print(y)  # 2025-02-12 00:00:00

print(x.year)  # .month (num) or .day (num)


print(x.strftime("%A"))
