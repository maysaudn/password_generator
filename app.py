import random
import string

print("Welcome to Your Password Generator")

lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation
all_chars = lowercase_chars + uppercase_chars + digits + special_chars

number_of_passwords = input("How many passwords do you need? ")
number_of_passwords = int(number_of_passwords)

password_length = input("Please enter the required length of your passwords: ")
password_length = int(password_length)

list_of_passwords = []

def get_password(length):
    password = ""
    for char in range(0, password_length):
        password += random.choice(all_chars)
    return password

while len(list_of_passwords) < number_of_passwords:
    potential_password = get_password(password_length)
    
    contains_special_char = None
    contains_digit = None
    contains_uppercase = None
    
    for i in range(0, len(potential_password)):
        if potential_password[i] in special_chars:
            contains_special_char = True
        elif potential_password[i] in digits:
            contains_digit = True
        elif potential_password[i] in uppercase_chars:
            contains_uppercase = True
        else:
            continue
    
    if contains_digit and contains_special_char and contains_uppercase:
        list_of_passwords.append(potential_password)
        
print("\nhere are your passwords:", *list_of_passwords, sep="\n")
