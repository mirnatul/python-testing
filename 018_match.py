day, month = 8, 3
match day:
    case 1 | 2 | 3 if month == 3:
        print("a")
    case 4 | 5 | 6:
        print("b")
    case 7:
        print("c")
    case _:
        print("Default")
