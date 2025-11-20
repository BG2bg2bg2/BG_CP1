#Welcome to the Flexible Calculator!

#Available operations: sum, average, max, min, product

#Which operation would you like to perform? average

#Enter numbers (type 'done' when finished):
#Number: 10
#Number: 15
#Number: 20
#Number: 25
#Number: done

#Calculating average of: 10, 15, 20, 25
#Result: 17.5

#Would you like to perform another calculation? (yes/no) yes

#Which operation would you like to perform? max

#Enter numbers (type 'done' when finished):
#Number: """42"""
#Number: """18"""
#Number: """91"""
#Number: """7"""
#Number: """63"""
#Number: """done"""

#Calculating max of: 42, 18, 91, 7, 63
#Result: 91

#Would you like to perform another calculation? (yes/no) 
"""no"""

#Thank you for using the Flexible Calculator!

#BG 1st flexible calculator

#statistics for the advarage
import statistics
import math
#list of numbers user puts in it
numbers = []
#num 

#for num in list(numbers):
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    choice = input("enter a number 1-5")
    user_input = input("Enter a number: ")

    if is_float(user_input):
        print("That is a float (or a valid number).")
        numbers.append(user_input)
        continue
    else:
        print("That is NOT a number.")

    for p in map(lambda num: (f"original: {num}", f"squared: {num**2}"), numbers):
        #display what the previous code made
        print(p)