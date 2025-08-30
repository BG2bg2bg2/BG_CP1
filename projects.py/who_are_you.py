#BG, 1st, Who are you
name = input("What is your name?")
age = input("May I ask how old you are?")
Yes = input("do you right 'becasue' for the start of a sencince if you hear or see the word 'why'? type 'yes', 'Yes', 'y' or 'Y' if no type what ever you want")
fav_color = input("What is your favorite color?")
if Yes == "yes" or "Yes" or "Y" or "y":
    why_fav_color = input(f"why is {fav_color} your favorite color(s)?")
    print(f"Hi, {name}. What was your favorit memory about {age} You like {fav_color} {why_fav_color}")
elif Yes != "yes" or "Yes" or "Y" or "y":
    why_fav_color = input(f"Why do you like {fav_color}")
    print(f"Hi {name} What do you like about being {age}? you like {fav_color} because {why_fav_color}")
    