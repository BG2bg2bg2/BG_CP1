#BG 1st order python

tax = .5

food = {
    "fries": 3,
    "chicken nuggets": 2.3
}

food1 = {
    "hamberger": 3,
    "cheesberger": 2,
    "salad": 3
}

drinks = {
    "root beer": .4,
    "sprite": .9,
    "DR Pepper": 2.3,
    "MTN Dew": .8,
    "Coca Cola": 2.1 
}

shopping_list = {}

while True:
    for a in food:
        print("curent list of food", food1)
        print("curent list of sides", food)
        print("curent list of drinks", drinks)
        if a in shopping_list >0:
            print("shopping list", shopping_list)
        choice = input("enter 'choose', 'pay', 'rid': ")
    if choice == "pay":
        print()
        break
    elif choice in ['choose', 'rid']:
        f = input(f"enter the name of the food: ")

        
