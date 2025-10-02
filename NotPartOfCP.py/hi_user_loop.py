greet = False
while greet == True:
    Hi = input("What does one usually say when they greet you? ")
    if Hi.isalpha() or Hi.isalnum():
        print(Hi)
    else:
        print("Something is wrong")