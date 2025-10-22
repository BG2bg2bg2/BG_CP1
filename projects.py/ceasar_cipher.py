#BG 1st ceasar cipher

list_code = []

def encode(phrase, shift):
    new_phrase = ""
    # Return error message if shift > 25 (there are 26 characters in the alphabet) or < 0
    # step through each character of the string
    for a in phrase:
        # get its ASCII value with ord(character) to get ASCII value
        old_ascii = ord(a)
        print(old_ascii)
        # Find out if lowercase or uppercase
        if old_ascii >= 65 and old_ascii <= 90:
            b = old_ascii + shift
            if b > 90:
                b -= 26
            print(b)
            new_phrase += chr(b)
        elif old_ascii >= 97 and old_ascii <= 122:
            c = old_ascii + shift
            if c > 122:
                c -= 26
            print(c)
            new_phrase += chr(c)
        else:
            new_phrase += a
        # add shift to the ASCII value
        
        # check to see if past Z or z and wrap to beginning of alphabet if needed
    
    # add character to new string  with chr(ascii)
    # return new phrase
    return new_phrase

code = True
# make sure the code can run till code == False
while code != False:
    # meant to help guild the user to know what to do
    print("welcome to ceasar cipher enter a number 1-5 \n 1 = enter letters to encrypt with shift defalt as 1 \n 2 = enter numbers to encrypt with shift defalt as 1 \n 3 = enter letters and choose how far you want to shift 25 is max \n 4 = enter numbers to encrypt and choose how far you want to shift 25 is the max \n 5 = quit")
    
    # enter a number
    choose = input(int("enter a number"))
    # for what is in choose depends on the out come
    for d in choose:
        if choose != choose.isdigit():
            print("try again")
            #restart the loop
            continue    

        elif choose.isdigit():
            if choose == 1:
                code1 = input("enter letters to encrypt defalt of 1")

                if code1.isalpha():
                    print(code1 + 1)
                elif code1.isdecimal() or code1.isdigit():
                    print("try again")
            if choose == 2:
                for e in list_code:
                    code1 = (input("enter numbers to encrypt with defalt of 1"))
                    list_code.append(code1)
    
        if code1 is code1.isdigit():
            c = chr(code1)
            print(c)
        elif code1 is complex():
            d=ord(code1)
            print(d)

