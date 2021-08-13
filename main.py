import string
import random

upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)
numbers = list(string.digits)
spec_char = list(string.punctuation)

password_list = []
password_list.extend(upper_case + lower_case + numbers + spec_char)


print("Welcome to PGenie- The Password Generator!\n")
pass_length = int(input("What length would you like your password to be?\n"))
pass_count = int(input("How many passwords you want to generate?\n"))


for i in range(1, pass_count + 1):
    random.shuffle(password_list)
    my_password = ("".join(password_list[0:pass_length]))
    print(f"Your {i} password is: {my_password}\n")
