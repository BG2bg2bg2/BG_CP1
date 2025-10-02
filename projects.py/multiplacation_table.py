#BG 1st Multipacation table
print("welcome to multiplactaion tables")
print("Rows are up and down while colomes are left and right")
table_colum = input("enter a number for colums going left to right")
if table_colum.isalpha():
    print("must be a number")
if table_colum.isdigit() and table_colum <= 12:
    table_row = input("enter another number for rows going up and down")
    if table_row.isalpha() and table_row <= 12:
        print("Must be a number")
        if table_row.isdigit():
            print("Continuing")
        
else:
    print("Something is wrong :(")
mt = False
while mt == False:
    Mt = input