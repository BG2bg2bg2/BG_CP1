#BG 1st flexible calculator

#statistics for the advarage

#list of numbers user puts in it

#num 

#for num in list(numbers):
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


user_input = input("Enter a number: ")

if is_float(user_input):
    print("That is a float (or a valid number).")
else:
    print("That is NOT a number.")