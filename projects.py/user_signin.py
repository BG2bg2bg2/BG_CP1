#BG 1st user_signin.py


#Remember to put our 1st line comment (initials, class period, assignment name)


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
                newus = input("Enter a last name")
                print(f"Your user name is {newus}")

#check for username

#Check for password

#Only output the welcome message if BOTH username and password are correct.
#


#Make sure your code works (test it 5 times with different numbers AND have your elbow partner test it!)

#Save your work

#Commit and push your code to Github

#Not my code
#           |
#           |
#          " "
#           '

#username6 = "notneeded23"
#password = "BLJDFI324lkjaekl#$#@lkj"
#user = input ("What is your username")
#pword = input ("What is your password")
#if not user or not pword:
#    print("Enter a valid input")
#elif user == "Love" and pword == "passweord":
#    print("Hello Love")
#
#if pword == "passweord":
#    print("Hello Love")
#else:
#    print("Incorect password")
#    pass
#if user == username6 and pword == password:
#    print("wellcom")
#elif user == username6:
#    print("Password incorect")
#else:
#    print("Incorect password")