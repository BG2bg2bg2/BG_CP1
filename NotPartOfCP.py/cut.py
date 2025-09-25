user_name1 = False
while user_name1 == False:
    fname1 = input("what is your first name?")
    if fname1 == "Steaven":
        break
    if fname1 == "Blop":
        break
    if fname1 != "Steaven" or "Blop":
        newu = input("Do you want to make a new user name 'yes' or 'not'?")
        if newu == "yes":
            lname = input("What is your last name")
            print(f"your username is now {fname1 + lname} welcome") 
        else:
            print("retry")
user_name1 = False
while user_name1 == False:
    lname1 = input("What is your lastname?")
    if lname1 == "Star":
        fname_lname1 = input("double checking but enenter you firts and last name example 'firtst.last'")
        if fname_lname1 == "Steaven.Star":
            print(f"wellcome {fname_lname1}")
            break    
    if lname1 == "Popper":
        fname_lname1 = input("Sorry for asking but could you enter you 'first.lastname'")
        if fname_lname1 == "Blop.Popper":
            print(f"I know you {fname_lname1}")
            break
    if (fname1) != "Steaven" and (lname1) != "Star":
        if (fname1) != "Blop" and (lname1) != "Popper":
            newu1 = input("Do you want to make a new user last name?")
            if newu1 == "yes":
                nun1 = input("Enter your first name")
                nun2 = input("enter your last name")
                if nun1 == nun1 and nun2 == nun2:
                    print(f"Your user name is {nun1}.{nun2}")
