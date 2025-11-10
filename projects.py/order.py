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


shop = []
while True:
    print("\n1 = add item.\n2 = remove item. \n3 = show list.\n4 = clear. \n5 = Quit")
    num = input("\nchoose a number 1-5 ")

    if num == "1":
        item = input("\nwhat is the item you want to add? ")
        shop.append(item)
        print(f"\n{item} has been added")

    if num == "2":
        item = input("\nwhat item do you want to remove? ")
        if item in shop:
            shop.remove(item)
            print(f"\n{item} removed")
        else:
            print(f"\n{item} not found")

    if num == "3":
        if shop:
            for a in enumerate(shop):
                #print({item}, {a})
                print("\n not going to work")
                print(list(shop))
        else:
            print("\nNo item on")

    if num == "4":
        print("\nclear")
        if shop:
            shop.clear()
            print("cleared")
    if num == "5":
        print(f"\nQuiting")
        break
    else:
        print("\ntry again")    
    