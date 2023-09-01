print("Welcome to the rollercoaster!")
height = int(input("What is your height?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $4.")
    elif age <= 18:
        print("Please pay $6.")
    else:
        print("Please pay $10.")
else:
    print("Sorry, but you can't ride the rollercoaster.")


