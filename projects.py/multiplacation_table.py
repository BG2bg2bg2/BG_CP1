#BG 1st multiplacation table

while True:
    print("Welcome to the multiplication table")
    colum = input("Enter a number for colum 1-12 ")
    row = input("enter a number for row 1-12 ")
    if not colum.isdigit() or not row.isdigit():
        print("Must be a number")
        continue    
    y = int(colum)+1
    if row.isdigit():
        x = int(row)+1
        if x > 22 or y > 22:
            print("both must be <= 21")
            continue
        for q in range(1, x):
            for d in range(1, y):
                print(f"{q*d:>{5}}",end="")
            print()
