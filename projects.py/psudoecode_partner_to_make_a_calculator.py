#BG 1st psudeocode partner factorial code
"""
diplay("welcome to the factorial calculator!")
    #origonal = number
number = input(number)
if number<0 or number is a decimal
display "please enter a non-decimal number or a non-negitive number"
#else if number>0
    pass

#else:
    invalid

numbers = []
while number> 1:
    number - 1
    numbers.append(number)
if number ==1

display("calculating")
for num in numbers num = numbers all multiplied with eachother
display:
"""


hi = "welcome to the facorial calculator" #just wanted to make global varialbe for no reason

#def get_num(): #needs a function because input validation is repeated logic and organizing code makes it reusable

def get_num(): #function to get a valid non-negative integer from the user
    while True: #this will help the user to not have to restart the program
        try:
            #origonal = number
            #number = input(number)
            number = input("Enter a number: ")
            #if number<0 or number is a decimal
            if not number.isdecimal() or int(number) < 0:
                #display "please enter a non-decimal number or a non-negitive number"
                print("pleas enter a non-decimal number or a non-negitive number")
                continue
            #else if number>=0
            elif int(number) >= 0:
                #    pass
                number = int(number)
                #return number
                return number
        except ValueError:
            #   invalid
            print("invalid try again:(")
            continue

#diplay("welcome to the factorial calculator!")
print(hi) #global varialbe is useful somtimes

#call the function to get user input
number = get_num() #using a function ensures input validation is clean and reusable

#numbers = []
numbers_list = []

#while number> 1:
temp_number = number
while temp_number > 1:
    #    number - 1
    temp_number -= 1
    #    numbers.append(number)
    numbers_list.append(temp_number + 1)  # store the correct sequence

#if number ==1
if number == 0 or number == 1:
    #display("calculating")
    print("calculating")

#for num in numbers num = numbers all multiplied with eachother
li = 1
for num in numbers_list:
    li *= num

#display:
print(f"factorial {number} is {li}")
