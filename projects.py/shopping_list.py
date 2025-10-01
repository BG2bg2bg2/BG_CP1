#BG 1st shopping list

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
    