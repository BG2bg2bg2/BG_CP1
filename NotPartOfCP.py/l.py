# Using a loop
list_of_dicts = []
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 24, 35]
cities = ['New York', 'London', 'Paris']

for i in range(len(names)):
    person = {'name': names[i], 'age': ages[i], 'city': cities[i]}
    list_of_dicts.append(person)

# Using list comprehension with zip (more concise)
keys = ['name', 'age', 'city']
values = [
    ['Alice', 30, 'New York'],
    ['Bob', 24, 'London'],
    ['Charlie', 35, 'Paris']
]

list_of_dicts_comprehension = [dict(zip(keys, v)) for v in values]