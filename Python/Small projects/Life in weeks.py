print("Let's say that you will live 90 years.\nDo you want to know how many months, weeks and days you have left?\nLet's find out!")


age = input("What is your current age? ")

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

message = f"You have {days} days, {weeks} weeks, and {months} months left."

print(message)


