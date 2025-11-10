#BG 1st dictionary notes
print("What are dictionaries?")
print("Dictionaries are a Python data structure that store information in key : value pairs inside { }.\n")

print("How do dictionaries simplify variables in a project?")
print("They allow you to store many related values under one single variable, making the code more organized and easier to manage.\n")

print("What are key and value pairs?")
print("A key is the label/name (veriable), and a value is the data stored for that label. Example: \"age\": 15\n")

print("How do you build a dictionary?")
print("Use {} with keys and values separated by colons.\nExample:\nperson = {\"name\": \"Alex\", \"age\": 15}\n")

print("How do you call a value from a dictionary?")
print("Use the key inside square brackets.\nExample:\nperson[\"name\"]\n")

print("How do you get each of the keys from a dictionary?")
print("Use the .keys() function.\nExample:\nperson.keys()\n")

print("How do you update a value in a dictionary?")
print("Reassign a new value to an existing key.\nExample:\nperson[\"age\"] = 16\n")

print("Can you add new key and value pairs to a dictionary during runtime?")
print("Yes! Just assign a value to a new key.\nExample:\nperson[\"school\"] = \"Central High\"\n")


#key: value pairs
person = {
    #key:value,
    "name": "Xavier",
    'age': 22,
    'job': "Mavrick",
    'sibling': ["Alex", "Katie", "andrew", "Vienna", "Tia", "Treyson", "Jake"]
}
person_two = {
    "name": "Alex",
    'age': 14,
    'job': "Mavrick",
    'sibling': ["Xavier", "Katie", "andrew", "Vienna", "Tia", "Treyson", "Jake"]
}
print(f"Name is {person["name"]}")
print(person.keys())


for key in person.keys():
    if key == "sibling":
        for name in person[key]:
            print(f"{person['name']} has a sibling named {name}")
        else:
            print(f"{key} is {person[key]}")

print(person.values())
person["age"] += 1
print(person.items())
print(person.keys())
person_two["SO"] = "Carry"
person["age"] += 1
print(person_two.items())

avatar = {
    "earth": {
        "toph": "Sounds like Tough and thats just what I am!"
    },
    "Water": {
        "Katara": "Itt just game me so much Hope",
        "Sokka": "I used to be boomerang guy"
    }
}

print(avatar['earth']['toph'])