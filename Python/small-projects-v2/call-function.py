def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


#greet()

# Function that allows for input:

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")


#greet_with_name("Dominika")

# Functions with more than 1 input:

"""def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today in {location}?")

greet_with("Dominika", "Ringsted")"""

# Function with keyword arguments:

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Isn't the weather nice today in {location}?")
    print(f"How do you do {name}?")
    

greet_with(name = "Dominika",location = "Ringsted")


