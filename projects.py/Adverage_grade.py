# BG 1st Adverage grade

class1 = int(input("What is your grade for 1st class?"))
class2 = int(input("What is your grade for 2nd class?"))
class3 = int(input("What is your grade for 3rd class?"))
class4 = int(input("What is your grade for 4st class?"))
class5 = int(input("What is your grade for 5st class?"))
class6 = int(input("What is your grade for 6st class?"))
class7 = int(input("What is your grade for 7st class?"))

class_A = (class1 + class2 + class3 + class4 + class5 + class6 + class7)
class_B = (class_A/7)
class_C = round(class_B, 2)
print(f"Your clas adverage is {class_C}")

ad = True
Num0 = 0
Num_C = int(input("How many classes do you have"))
while ad == True:
    if Num0 < Num_C:
        Num_C1 = int(input("What is the class adverage"))
        Num0 += 1
        print(f"Class advrage = {Num_C}")
else:
    ad == False
    