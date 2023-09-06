print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 4
        print("Child tickets are $4.")
    elif age <= 18:
        bill = 6
        print("Youth tickets are $6.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 10
        print("Adult tickets are $10.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}. Enjoy your ride!")
        
else:
    print("Sorry, but you can't ride the rollercoaster.")


