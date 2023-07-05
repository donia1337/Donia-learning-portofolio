print("Hello dominika");

if 5 > 2:
 print("Five is greater than two!")

x = 5
y = "Hello, World!"

print(x)
print(y)

#A variable is created the moment you first assign a value to it.

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

a = 5
a=10

print(a)

#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(z)

#You can get the data type of a variable with the type() function.

x = 5
y = "John"
z = 5.0
print(type(x))
print(type(y))
print(type(z))


#Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a

"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


#Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)


#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python print() function is often used to output variables. In the print() function, you output multiple variables, separated by a comma. 
#You can also use the + operator to output multiple variables. For numbers, the + character works as a mathematical operator.
#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error.
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types.

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)


#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
#The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.


def myfunc():
  global x
  x = "very nice and seems easier than this stupid javascript"

myfunc()

print("Python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



#In programming, data type is an important concept.
#Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories


"""
TEXT TYPE: str
NUMERIC TYPES: int, float, complex
SEQUENCE TYPES: list, tuple,range
MAPPING TYPE: dict
SET TYPES: set, frozenset
BOOLEAN TYPE: bool
BINARY TYPES: bytes, bytearray, memoryview
NONE TYPE: NoneType
"""


#You can get the data type of any object by using the type() function.

x = 5
print(type(x))




