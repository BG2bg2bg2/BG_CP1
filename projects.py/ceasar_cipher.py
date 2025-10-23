#BG 1st ceasar cipher


def encode(phrase, shift):
    new_phrase = ""
    # Return error message if shift > 25 (there are 26 characters in the alphabet) or < 0
    # step through each character of the string
    for a in phrase:
        # get its ASCII value with ord(character) to get ASCII value
        old_ascii = ord(a)
        # Find out if lowercase or uppercase
        if old_ascii >= 65 and old_ascii <= 90:
            b = old_ascii + shift
            if b > 90:
                b -= 26
            new_phrase += chr(b)
        elif old_ascii >= 97 and old_ascii <= 122:
            c = old_ascii + shift
            if c > 122:
                c -= 26
            new_phrase += chr(c)
        else:
            new_phrase += a
        # add shift to the ASCII value
    return new_phrase

def decode(phrase, shift):
    new_phrase = ""
        
    # step through each character of the string
    for a in phrase:
        # get its ASCII value with ord(character) to get ASCII value
        old_ascii = ord(a)
        # Find out if lowercase or uppercase
        if old_ascii >= 65 and old_ascii <= 90:
            b = old_ascii - shift
            if b < 65:
                b += 26
            new_phrase += chr(b)
        elif old_ascii >= 97 and old_ascii <= 122:
            c = old_ascii - shift
            if c < 97:
                c += 26
            new_phrase += chr(c)
        else:
            new_phrase += a

        # check to see if past Z or z and wrap to beginning of alphabet if needed
    
    # add character to new string  with chr(ascii)
    # return new phrase
    return new_phrase


# make sure the code can run till code == False
while 1 == 1:
    # meant to help guild the user to know what to do
    print("welcome to ceasar cipher enter letters \n e = encode \n d = decode \n q = quit")
    
    # enter a letter
    choice = input("enter a letter e, d, q: ")
    if choice != "q" and choice != "e" and choice!= "d":
        print("try again")
        continue
    else:
        if choice == "q":
            break

    # for what is in choose depends on the out come
    
        phrase1 = input("enter phrase: ")
        shift1 = input("enter how many letters to shift: ")
        if shift1.isdigit():
            # Return error message if shift > 25 (there are 26 characters in the alphabet) or < 0
            shift1 = int(shift1)
            if shift1 > 26:
                #code wont run if true 
                print("must be btween 0 and 26")
                #restart the prosess
                continue
            else:
                if choice == "e":
                    #send letters forward
                    print(encode(phrase1, shift1))
                elif choice == "d":
                    #send letters backward.
                    print(decode(phrase1, shift1))