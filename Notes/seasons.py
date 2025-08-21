# BG 1st Seasons
#name = input("What is your last name?")
#season = input("What is your favorite season?")
#print(f"Wow {name} san, I like {season} too!")

name = input("What is your last name?")
season = input("What is your favorite season?")

if season == ("spring") or season == ("Spring"):
    print("Wow " + name + " San, I like"+ season + "too!")
elif season == ("summer") or season == ("summer"):
    print("Wow " + name + " San, I like " + season + " too!")
elif season == ("fall") or season == ("Fall"):
    print("Wow " + name + " San, I like " + season + " too!")
elif season == ("winter") or season == ("Winter"):
    print("Wow " + name + " San I like " + season + " too!")
else:
    print("Choose a season that is spelled because you missed spelled or chose a season that is not a season")