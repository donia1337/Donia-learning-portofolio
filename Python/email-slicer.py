# Small project of email slicer where we input email addresses to slice it into two parts. 

print('Please type your email address:')
email = str(input())

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} and domain is {domain}")

