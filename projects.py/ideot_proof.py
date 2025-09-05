#BG 1st ideot proofing

fname = input("enter your first name")
if len(fname) > 47:
    print("your name can't be over 47 leters")
elif not fname.find(" ") == -1:
    print("no spaces allowed for first name")
elif not fname.isalpha():
    print("Your name cant have numbers")
else:
    lname = input("enter your last name")
    if len(lname) > 746:
        print("last name is too long and only one man had it that long ever recoded")
    elif not lname.find(" ") == -1:
        print("must not have spaces")
    elif not lname.isalph():
        print("last name must not have have numbers")
    else:
        gpa = input("enter your gpa")
        if len(gpa) > 4:
            print 
