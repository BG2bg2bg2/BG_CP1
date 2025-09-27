# BG 1st What is my grade

# grade rules for some young aged classes
#A/ 94 | A-/ 90 | B+/ 87 | B/ 84 | B-/ 80 | C+/ 77 | C/ 74 | C-/ 70 | D+/ 67 | D/ 64 | D-/ 60 | F/ 0
LG = False
while LG == False:
    #Try make the code run unless false
    try:
        #This part is an input if one puts in a float it will be valid otherwise it syn error
        grade = float(input("Enter your grade "))
        #converts the int into an f statement leaving some words and space for the other words that will follow latter on
        result_begin = (f"Your score {grade}% is ")
        #anything greater than 94 is an A no A+
        if grade >= 94:
            result_end = "an A"
        #else is a, "since the previce is False then force this code to run True" but elif is "since the others is/are False then see if this is True or False else move on" 
        elif grade < 94 and grade >= 90:
            result_end = "an A-"
        elif grade < 90 and grade >= 87:
            result_end = "a B+"
        elif grade < 87 and grade >= 84:
            result_end = "a B"
        elif grade < 84 and grade >= 80:
            result_end = "a 'B-'"
        elif grade < 80 and grade >= 77:
            result_end = "a 'C+'"
        elif grade < 77 and grade >= 74:
            result_end = "a 'C'"
        elif grade < 74 and grade >= 70:
            result_end = "a 'C-'"
        elif grade < 70 and grade >= 67:
            result_end = "a 'D+'"
        elif grade < 67 and grade >= 64:
            result_end = "a 'D'"
        elif grade < 64 and grade >= 60:
            result_end = "a 'D-'"
        else:
            result_end = "an 'F'"
        #stops the wile loop from restarting and moves onto the nonindented parts connected to the While loop.
        break
    except:
        print("try again")
print(result_begin + result_end)

