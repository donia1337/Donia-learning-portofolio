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

#Three numeric types: 
  #int
    #float
      #complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex


#To verify the type of any object in Python, use the type() function.

print(type(x))
print(type(y))
print(type(z))


#INT
  #Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#FLOAT
  #Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


      #Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#COMPLEX
  #Complex numbers are written with a "j" as the imaginary part.

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#You can convert from one type to another with the int(), float(), and complex() methods.
  #Note: You cannot convert complex numbers into another number type.
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#Python does not have a random() function to make a random number, 
  #but Python has a built-in module called random that can be used to make random numbers.


import random

print(random.randrange(1, 10))

#There may be times when you want to specify a type on to a variable. This can be done with casting. 
  #Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
    #Casting in python is therefore done using constructor functions.
  #int() - constructs an integer number from an integer literal, 
    #a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
  #float() - constructs a float number from an integer literal, 
      #a float literal or a string literal (providing the string represents a float or an integer)
  #str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

#INT:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#FLOATS

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#STRINGS

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



#You can assign a multiline string to a variable by using three quotes """. Or three single quotas. '''

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Get the character at position 1 (remember that the first character has the position 0).

a = "Hello, World!"
print(a[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop.
#Loop through the letters in the word "banana"

word = "banana"
for letter in word:
  print(letter)

for x in "banana":
  print(x)


#To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
#Check if "free" is present in the following text.

txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.


txt = "The best things in life are free!"
print("expensive" not in txt)

#Use it in an if statement.

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
print(b[2:5])

#By leaving out the start index, the range will start at the first character.
#Get the characters from the start to position 5 (not included).

b = "Hello, World!"
print(b[:5])

#By leaving out the end index, the range will go to the end.

b = "Hello, World!"
print(b[2:])

#Use negative indexes to start the slice from the end of the string.
#Get the characters, From: "o" in "World!" (position -5), To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])


#The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())  

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip())

#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("World", "Earth"))

#The split() method splits the string into substrings if it finds instances of the separator.

a = "Hello, World!"
print(a.split(","))

#To concatenate, or combine, two strings you can use the + operator.

#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

print ('hello world')

# To combine strings and numbers together you can do that using format() function.
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escpare character
# An escape character is a backslash \ followed by the character you want to insert.
# Example: txt = "We are the so-called "Vikings" from the north."
# To fix this problem, use the escape character \":

txt = "We are the so-called \"Vikings\" from the north."

# Booleans represent one of two values: True or False.

print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
# the number 0, and the value None. And of course the value False evaluates to False.


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# One more value, or object in this case, evaluates to False, 
# and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# You can create functions that returns a Boolean Value:

def myFunction() :
  return True

print(myFunction())

# You can execute code based on the Boolean answer of a function:
# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# Python also has many built-in functions that return a boolean value, 
# like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))


# The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables). 
# The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.


def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# We could have achieved the same result more easily by using lambda syntax.

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

# The function filter filters an iterable by leaving only the items that match a condition (also called a predicate).
# (Like map, the result has to be explicitly converted to a list if you want to print it.)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)














