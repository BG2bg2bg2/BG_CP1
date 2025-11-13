#BG 1st order python

# universal variable for tax
tax = 0.05  # 5% tax


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
    "hamburger": {"cost": 3},
    "cheeseburger": {"cost": 2.3},
    "salad": {"cost": 3.7},
    "PBJ": {"cost": 4}
}

# drinks dictionary
drinks = {
    "root beer": 0.4,
    "sprite": 0.9,
    "MTN Dew": 0.8,
    "Coca Cola": 2.1
}


# function to display menu
def display_sides(menu):
    print("\nSides Menu:")
    for key in menu.keys():
        #show the number
        print(f"{key}. {menu[key]['name']} (${menu[key]['cost']})")


# start order system
order = []

while True:
    #display options for ordering
    print("\n1 = choose from the sides")
    print("2 = choose from the main course")
    print("3 = choose from the drinks")
    print("4 = remove item")
    print("5 = show list of ordered items")
    print("6 = pay and exit")


    #promt user to choose a number in the options
    num = input("\nChoose a number 1-6: ")

    # SIDES choice
    if num == "1":
        display_sides(sides)
        s = input("Choose a side number: ")
        #see if the choice is in the side dictionary
        if s in sides:
            #puts the wanted option into the order list
            order.append(sides[s]["name"])
            print(f"Added {sides[s]['name']}")
        else:
            #if the option doesnt exist restart
            print("That side doesn't exist.")
            continue

    # MAIN COURSE
    elif num == "2":
        #print the main course options
        print("\nMain Course Options:")
        for k, v in main_course.items():
            print(f"- {k} (${v['cost']})")
        m = input("Enter your main course: ")
        if m in main_course:
            order.append(m)
            print(f"Added {m}")
        else:
            print("That's not on the menu.")

    # DRINKS
    elif num == "3":
        print("\nDrinks Menu:")
        for k, v in drinks.items():
            print(f"- {k} (${v})")
        d = input("Enter your drink: ")
        if d in drinks:
            order.append(d)
            print(f"Added {d}")
        else:
            print("Drink not available.")

    # REMOVE ITEM
    elif num == "4":
        item = input("What item do you want to remove? ")
        if item in order:
            order.remove(item)
            print(f"{item} removed.")
        else:
            print("That item is not in your order.")

    # SHOW ORDER
    elif num == "5":
        if order:
            print("\nYour current order:")
            for i, o in enumerate(order, 1):
                print(f"{i}. {o}")
        #if there is nothing in the order show empty order
        else:
            print("Your order is empty.")

    # PAY AND EXIT
    elif num == "6":
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
            for s in sides.values():
                #if there is any sides do the following
                if s["name"] == o:
                    #calculates how much you have and need to pay for sides
                    total += s["cost"]
                #if there is any main course options do the following
            for m in main_course.keys():
                if m == o:
                    #calculate the amount in the main course
                    total += main_course[m]["cost"]
            for d in drinks.keys():
                #if there is any drinks do the folloing
                if d == o:
                    #calculat the amount of drink costs
                    total += drinks[d]

        total += total * tax
        print(f"\nYour total (with tax): ${round(total, 2)}")
        print("Thank you for your order!")
        break

    else:
        print("Invalid choice. Try again.")
