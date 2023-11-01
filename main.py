import pyshorteners
import random
import string

# URL SHORTENER (implements pyshorteners)
def URL():
    long_url = input("Enter URL to shorten: ")
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)

    print("Orignal URL: " + long_url)
    print("Shortened URL: " + short_url)


#password generator
def password():
    length = int(input("Enter length of password: "))
    all = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(all,length))
    print("Password: " + password)

print("Welcome to Tiny Functions 0.1!")
user = 0


while (user==0):
    print("1 - URL Shortener")
    print("2 - Password Generator")
    choice = int(input("Select your function of choice (Indicate with number): "))
    if (choice == 1):
        URL()
    elif (choice == 2):
        password()
    else:
        print("Indicate a valid number.")
    choice2 = int (input("Would you like to use another function? (Select 1 for Yes, 2 for No)"))
    if (choice2 == 2):
        exit()

