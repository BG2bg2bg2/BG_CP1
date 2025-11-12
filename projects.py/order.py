#BG 1st order python

tax = .5
#food for the sides
sides = {
    "fries": {"cost": 3, "amount": 0},
    "chicken nuggets":{"cost": 2.3, "amount": 0},
    "roles": {"cost": 2, "amount": 0},
    "muffins": {"cost": 2.9, "amount": 0}
}
#main food corse
main_corse = {
    "hamberger": {"cost": 3, "amount": 0},
    "cheesberger": {"cost": 2.3, "amount": 0},
    "salad": {"cost": 3.7, "amount": 0},
    "PBJ": {"cost": 4, "amount": 0}
}
#drinks
drinks = {
    "root beer": .4,
    "sprite": .9,
    "MTN Dew": .8,
    "Coca Cola": 2.1 
}


shop = []
while True:
    
    print("\n1 = choose from the sides\n2 = choose from the main corse. \n3 = choose from the drinks.\n4 = check out")
    num = input("\nchoose a number 1-5 ")

    if num == "1":
        print("\nCurrent sides:", sides)
    action = input("enter 'add', 'pay', or 'next': ").lower()

    if action == "next":
        continue
    elif action in ['add', 'pay']:
        order = input("enter your order: ")
        quantity = int(input("enter quantity: "))

        if action == "add":
            sides[shop] = order
        else:
            if sides in order:
                shop.append(order)
            else:
                print("Error: not enough stock or book not found")
    else:
        print("Invalid action. Please try again")
        continue

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