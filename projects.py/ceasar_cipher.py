#BG 1st ceasar cipher


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
            p = old_ascii + shift
            if p > 90:
                p -= 26
            print(p)
            new_phrase += chr(p)
        elif old_ascii >= 97 and old_ascii <= 122:
            l = old_ascii + shift
            if l > 122:
                l -= 26
            print(l)
            new_phrase += chr(l)
        else:
            new_phrase += a
        # add shift to the ASCII value
        
        # check to see if past Z or z and wrap to beginning of alphabet if needed
    
    # add character to new string  with chr(ascii)
    # return new phrase
    return new_phrase

print("welcome to ceasar cipher")
print("enter a phrase and I will encrypt it for you")
code1 = input("enter phrase here: ")
print(encode(code1, 1))

if code1 is code1.isdigit():
    c = chr(code1)
    print(c)
elif code1 is complex():
    d=ord(code1)
    print(d)

