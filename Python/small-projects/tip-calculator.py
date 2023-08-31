print("Welcome to the tip calculator! :)")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

if tip == 0:
    print("You're a cheap person!")
    quit()



people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
# print(bill_with_tip)

bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}. Hope you enjyoed your meals!")





