#BG 1st order python

cost = .76

#Create a program that allows a user to order items off a menu.


#  Menu items need to be stored in a dictionary with their prices as the value.

num_drinks = {
    "root beer": .92,
    "Mountain dew": .23,
    "Slerpy": .24,
    "Dr pepper": .98
}
drink = [num_drinks]


#  Users need to be able to order a drink, a main course and two side dishes.

for a in num_drinks:
    choice = input("Enter a leter a-f")
    print("a = choose a drink")
    if choice == "a" or choice == "A":
        print(num_drinks["root beer"])

# At the end the program needs to repeat back to the user their full order, and the total cost. 