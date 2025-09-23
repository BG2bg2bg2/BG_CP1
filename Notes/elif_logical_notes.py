# BG 1st Logical Oporators

grade = 100

if grade > 100:
    print(f"You have an 'A' and you did extra credit... you did this much extra credit {grade - 100}%")
elif grade == 100:
    print("You have a perfict grade")
elif grade <= 98:
    if grade >= 92:
        print("You have an 'A'")
    elif grade < 92:
        if grade > 82:
            print("You have a 'B'")
        elif 