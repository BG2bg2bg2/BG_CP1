#BG 1st order python

tax = .5
#food for the sides
#dictonary
sides = {
    #diction in dictionary
     "1": {"name": "fries", "cost": 3},
    "2": {"name": "chicken nuggets", "cost": 3},
    "3": {"name": "roles", "cost": 3},
    "4": {"name": "muffins", "cost": 3}
}
#main food corse
main_corse = {
    "hamberger": {"cost": 3},
    "cheesberger": {"cost": 2.3,},
    "salad": {"cost": 3.7},
    "PBJ": {"cost": 4}
}
#drinks
drinks = {
    "root beer": .4,
    "sprite": .9,
    "MTN Dew": .8,
    "Coca Cola": 2.1
}

def display_menu(menu):
    for a in menu.keys():
        print(a, menu.get(a).get("name"))

order = []
while True:
    display_menu(sides)
    break
    print("\n1 = choose from the sides\n2 = choose from the main corse. \n3 = choose from the drinks.\n4 = check out")
    num = input("\nchoose a number 1-5 ")

    if num == "1":
        print("\nCurrent sides:", sides)
    action = input("enter '1' add, '2' dislay menu, or '3' next: ").lower()

    if action == "1":
        continue
    elif action in ['add', 'pay']:
        item = input("enter your order: ")
        quantity = int(input("enter quantity: "))

        if action == "add":
            sides[order] = ite
        else:
            if sides in item:
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
