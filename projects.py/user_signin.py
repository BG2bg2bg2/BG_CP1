#BG 1st

#Name your file user_signin.py


#Remember to put our 1st line comment (initials, class period, assignment name)



us1 = True
while us1 == False:
    def first_user_name(us1):
        try:
            float(str.us1)
            return True
        except ValueError:
            print("Somethings is wrong")

#You will need 2 user inputs
us1

first_name1 = input("what is your first name")
if float(first_name1) >=0:
    print("must me a name")
if float(first_name1) <=0:
    print("Not going to work must be a name")
elif str(first_name1) >= len(15):
    print("shorten your user name")
else:
    last_name1 = input("what is your last name")
    if float(last_name1) >=0:
        print("Nice try must be a last name")
    if float(last_name1) <=0:
        print("Must be a last name")
    elif last_name1 == first_name1:
        print("Make up a last name")
print(first_name1 + last_name1)

#check for username

#Check for password

#Only output the welcome message if BOTH username and password are correct.
#


#Make sure your code works (test it 5 times with different numbers AND have your elbow partner test it!)

#Save your work

#Commit and push your code to Github