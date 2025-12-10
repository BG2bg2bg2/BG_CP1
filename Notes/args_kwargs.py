#BG 1st *args and **kwargs

#hi
def hello(*names, **kwargs):
    print(type(names))
    print(kwargs)
    print(type(kwargs))
    for n in names:
        print(f"hello {n} {kwargs['last_name']}")

hello("B", "G", "v", "x", "L", last_name="G", dad="L", num_dogs=3)


def full_name(age, **names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['middle']} {names['last']} is {age}"
    else:
        return f"{names['first']} {names['last']} is {age}"

print(full_name(age="???", first="karo", last="sensa"))
print(full_name(age="so old", first="albus", middle="brian", last="dubuldore"))


def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum += f"{story['name']} is the main character of the story. "
    if "place" in story.keys():
        sum += f"The story takes place in {story['place']}. "
    if "confict" in story.keys():
        sum += f"The problem is {story['confict']}."
    return sum

print(summary(name="luke skywalker", place="galaxy far far away", confict="rescue the princess"))
print(summary(name="Harry potter", confict="Kill the dark lord"))


chat = {
    "What are positional arguments?": 
        (
            "Positional arguments must be passed in the correct order.\n"
            "Example:\n"
            "def greet(name, age):\n"
            "    print(name, age)\n"
            "greet('Alice', 15)\n"
        ),

    "What are keyword arguments?": 
        (
            "Keyword arguments include the parameter name so order doesn't matter.\n"
            "Example:\n"
            "def greet(name, age):\n"
            "    print(name, age)\n"
            "greet(age=15, name='Alice')\n"
        ),

    "How do you set a default parameter value?": 
        (
            "Give a parameter a default value in the function definition.\n"
            "Example:\n"
            "def greet(name='Guest'):\n"
            "    print('Hello,', name)\n"
            "greet()\n"
            "greet('Hi')\n"
        ),

    "How do you alter a function to take in an unknown number of arguments?": 
        (
            "Use *args for unlimited positional arguments and **kwargs for unlimited keyword arguments.\n"
            "Examples:\n"
            "def add_numbers(*args):\n"
            "    print(args)\n"
            "add_numbers(1, 2, 3)\n\n"
            "def describe_person(**kwargs):\n"
            "    print(kwargs)\n"
            "describe_person(name='Bob', age=100)\n"
        )
}

for question, answer in chat.items():
    print(question)
    print(answer)
    print("-" * 50)
