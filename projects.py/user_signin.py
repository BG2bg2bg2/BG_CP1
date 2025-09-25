#BG 1st user_signin.py
uname1 = "Hipo"
pw1 = "Lolo"
#get username
user_name = input("Enter your username ")

#get password
password = input("Enter your Password pls ")

#Welcome if user and pass match
if uname1 == user_name and pw1 == password:
    print(f"Welcome, {user_name}")
else:
    print("Invalid credentials aka info.")