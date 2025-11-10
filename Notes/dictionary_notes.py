#BG 1st dictionary notes

#What are dictionaries?

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
#How do dictionaries simply variables in a project?



#What are key and value pairs?



#How do you build a dictionary?



#How do you call a value from a dictionary?



#How do you get each of the keys from a dictionary?



#How do you update a value in a dictionary?



#Can you add new key and value pairs to a dictionary during runtime?




