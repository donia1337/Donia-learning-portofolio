# Complete the program to get a string as input, 
# search for the name in the list of contacts and output the age of the contact in the format presented below:

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()


for x in contacts:
    if name in x:
        print(str(x[0]) + " is " + str(x[1]))
        break
else:
    print("Not Found")