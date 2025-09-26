# BG 1st What is my grade

#A/ 94 | A-/ 90 | B+/ 87 | B/ 84 | B-/ 80 | C+/ 77 | C/ 74 | C-/ 70 | D+/ 67 | D/ 64 | D-/ 60 | F/ 0
LG = False
while LG == False:
    try:
        grade = float(input("Enter your grade"))
        if grade > 100:
            print(f"you have extra credit with {grade - 100}")
        if grade <= 100 and grade >= 94:
            print("You have and 'A'")
        if grade < 94 and grade >= 90:
            print("You have an 'A-'")
        if grade < 90 and grade >= 87:
            print("You have a 'B+'")
        if grade < 87 and grade >= 84:
            print("you have a B")
        if grade < 84 and grade >= 80:
            print("You have a 'B-'")
        if grade < 80 and grade >= 77:
            print("you have a 'C+'")
        if grade < 77 and grade >= 74:
            print("You have a 'C'")
        if grade < 74 and grade >= 70:
            print("You have a 'C-'")
        if grade < 70 and grade >= 67:
            print("You have a 'D+'")
        if grade < 67 and grade >= 64:
            print("You have a 'D'")
        if grade < 64 and grade >= 60:
            print("You have a 'D-'")
        if grade < 60 and grade >= 0:
            print("You have an 'F'")
        break
    except:
        print("try again")

    print(f"you have extra credit with {grade - 100}")
