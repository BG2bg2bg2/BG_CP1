#BG 1st crew shares


while True:
        print("The crew earned a whole bunch of $ on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. ")
        break

while True:
        m = int(input("how much money did the ship earn "))
        if m <= 500:
            print("This is too little amount of money")
        if m == 500:
            print("make sure that the crew number is enough to pay the captanin and first mate")
        break


l = int(input ("What is the amount of crew members excluding captain and first mate"))
       
ca = int(l * 500)
c = int(ca - m)
crew = c
cap = 7 / (m)
f_mate = 3 / (m)

print(f"There is crew that eraned ${crew} and captain earns ${cap} and first mate earned ${f_mate} ")