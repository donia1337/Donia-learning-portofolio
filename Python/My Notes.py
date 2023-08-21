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


# Generators are a type of iterable, like lists or tuples. 
# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops. 
# They can be created using functions and the yield statement.

def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)


# Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists. 
# In fact, they can be infinite!

def infinite_sevens():
  while True:
    yield 7
        
for i in infinite_sevens():
  print(i)

# In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
# Finite generators can be converted into lists by passing them as arguments to the list function.

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

# Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage. 
# Furthermore, we do not need to wait until all the elements have been generated before we start to use them.

# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# A list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
""""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# Print second item in the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Note: The search will start at index 2 (included) and end at index 5 (not included)

# By leaving out the start value, the range will start at the first item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# To change the value of a specific item, refer to the index number:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Add the elements of tropical to thislist:
# To append elements from another list to the current list, use the extend() method.


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#  The del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.

thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list. The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# You can loop through the list items by using a for loop:
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, 
# then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.


#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax

newlist = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.

# The condition is like a filter that only accepts the items that valuate to True.

# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
# The condition is optional and can be omitted:
# With no if statement:
newlist = [x for x in fruits]

# The iterable can be any iterable object, like a list, tuple, set etc.

# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

# Same example, but with a condition:
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

# The expression is the current item in the iteration, 
# but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]

# Customize Sort Function
# Customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: 
# list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join two lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""
                List Methods     
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""


# Python Tuples

mytuple = ("apple", "banana", "cherry")

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0] etc.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# To determine how many items a tuple has, use the len() function:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")

# It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

"""
List - is a collection which is ordered and changeable. Allows duplicate members.
Tuple - is a collection which is ordered and unchangeable. Allows duplicate members.
Set - is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary - is a collection which is ordered** and changeable. No duplicate members.
"""

# Access typles by index

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# By leaving out the start value, the range will start at the first item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# By leaving out the end value, the range will go on to the end of the list:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Specify negative indexes if you want to start the search from the end of the tuple:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# To determine if a specified item is present in a tuple use the in keyword:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, 
# you can convert it into a list, add your item(s), and convert it back into a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, 
# so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove items in tuples
# Tuples are unchangeable, 
# so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Or you can delete the tuple completely:
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


# You can also loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# You can loop through the tuple items by using a while loop.
# Use the len() function to determine the length of the tuple, t
# hen start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

"""
  Tuple Method
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""
















