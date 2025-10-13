#BG 1st pseudocode pass checker


#user score == 0 

user_score = 0

#spectial charitcers
spectial_chericers = "!@#$%^&*()_+~`_+-={}|[];':<>?,./\\"
#numbers needed
num = '1234567890'

#for the pass to see if it has any of these
Upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"

#for the index latter on to see if pass has any of these
lower = "qwertyuioplkjhgfdsazxcvbnm"
#enter a password
user_pass = input("enter pass")

#Loop until false
code = True
while code != False:
#check to see if there is numbers
    for i in user_pass:
        if i in num:
            #user score + 1 if true
            user_score = user_score + 1
            continue
#check to see if there is lower letters
    for l in user_pass:
        if l in lower:
            #user score + 1 if ture
            user_score = user_score +1
            continue
#check to see if there is Upber letters
    for a in user_pass:
        if a in Upper:
            user_score = user_score +1
            continue
#check if there is special characters
    for b in user_pass:
        if a in spectial_chericers:
            user_score = user_score + 1
            continue
#check to see if the password is 8 long
    for c in user_pass:
        if c in len(user_pass) >= 8:
            user_pass = user_pass + 1
            continue
    print(user_score)
    code == False