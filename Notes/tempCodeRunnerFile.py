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
            "greet('Brett')\n"
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
