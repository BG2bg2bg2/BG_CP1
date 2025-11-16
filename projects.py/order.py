#BG 1st order python

# universal variable for tax
tax = 0.05  # 5% tax
# start order system
order = []


#dictionary for foods for the sides
sides = {
    # dictionary in dictionary
    "1": {"name": "fries", "cost": 3},
    "2": {"name": "chicken nuggets", "cost": 3},
    "3": {"name": "rolls", "cost": 3},
    "4": {"name": "muffins", "cost": 3}
}

# main food course dictionary
main_course = {
    '1':{"name":"hamburger", "cost": 3},
    "2":{"name": "cheeseburger", "cost": 2.3},
    "3":{"name":"salad", "cost": 3.7},
    "4":{'name':"PBJ", "cost": 4}
}

# drinks dictionary
drinks = {
    "1":{"name":"root beer", "cost" : 0.4},
    "2":{"name":"sprite", "cost": 0.9},
    '3':{"name":"MTN Dew","cost": 0.8},
    '4':{"name":"Coca Cola", "cost": 2.1}
}


# function to display menu
def display_menu(menu):
    print("\nSides Menu:")
    for key in menu.keys():
        #show the number
        print(f"{key}. {menu[key]['name']} (${menu[key]['cost']})")

    s = input("Choose an item number: ")
    #see if the choice is in the dictionary
    if s in menu:
    #puts the wanted option into the order list
        order.append(menu[s])
        print(f"Added {menu[s]['name']}")
    else:
        #if the option doesnt exist restart
        print("That item doesn't exist.")


while True:
    #display options for ordering
    print("\n1 = choose from the sides")
    print("2 = choose from the main course")
    print("3 = choose from the drinks")
    print("4 = show list of ordered items")
    print("5 = pay and exit")


    #promt user to choose a number in the options
    num = input("\nChoose a number 1-5: ")

    # SIDES choice
    if num == "1":
        display_menu(sides)

    # MAIN COURSE
    elif num == "2":
        #print the main course options
        display_menu(main_course)

    # DRINKS
    elif num == "3":
         display_menu(drinks)


    # SHOW ORDER
    elif num == "4":
        if order:
            print("\nYour current order:")
            for i, o in enumerate(order, 1):
                print(f"{i}. {o["name"]} ${o["cost"]:.2f}")
        #if there is nothing in the order show empty order
        else:
            print("Your order is empty.")

    # PAY AND EXIT
    elif num == "5":
        #if user not ordered then show nothing ordered
        if not order:
            print("You haven't ordered anything yet!")
            #restart loop
            continue

        #start paying proses
        print("\nCalculating total...")
        total = 0

        #loop through what user ordered and the cost of each item
        for o in order:
            print(f'{o["name"]} ${o["cost"]:.2f}')
            #calculates how much you have and need to pay for sides
            total += o["cost"]


        #calculates how much the tax is and makes it into the total
        total1 = total *(1 + tax)
        #display total no tax included
        print(f"\nYour total (not tax): ${total: .2f}")
        #display total tax included
        print(f"\nYour total (with tax): ${total1: .2f}")
        print("Thank you for your order!")
        #end loop
        break
# if the user inputs the wrong stuff try again
    else:
        print("Invalid choice. Try again.")
