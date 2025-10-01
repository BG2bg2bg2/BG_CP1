#BG 1st shopping list

shop = []
while True:
    print("\n1 = add item.\n2 = remove item. \n3 = show list.\n4 = done")
    num = input("\nchoose a number 1-4 ")

    if num == "1":
        item = input("\nwhat is the item you want to add? ")
        shop.append(item)
        print(f"\n{item} has been added")

    elif num == "2":
        item = input("\nwhat item do you want to remove? ")
        if item in shop:
            shop.remove(item)
            print(f"\n{item} removed")
        else:
            print("\n{item} not found")

    elif num == "3":
        if shop:
            for a in enumerate(shop, 1):
                print(f"\n{a}, {item}")
        else:
            print("\nNo item on")

    elif num == "4":
        print("\nquiting")
        break
    else:
        print("\ntry again")    
    