"""
    INSTRUCTION:
        - Write a program that generates a password by taking certain parameters from users.
        - Parameters like:
            - Total number of letters in your password.
            - Number of alphabet in your password.
            - Number of symbols in your password.
            - Number of numbers in your password.
            
            easy lvl = abc12@#
            hard lvl = z%b8C#7
"""

import random


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A", "B", "C", "D", "E", "F"\
, "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbol = ["@", "$", "&", "_", "₹", "-", "=" ]

nr_alphabet = int(input("How many alphabet would you like in your password?\n"))
nr_symbol = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy level
password = ""
# let nr_letters = 4
for char in range(1, nr_alphabet + 1 ):
    # 1 - 4
    # random_alphabet = random.choice(alphabet)
    # password += random_alphabet
    password += random.choice(alphabet)
    
for char in range(1, nr_symbol + 1):
    password += random.choice(symbol)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

# Hard level
# z%b8C#7
password_list = []
# let nr_letters = 4
for char in range(1, nr_alphabet + 1 ):
    # 1 - 4
    # random_alphabet = random.choice(alphabet)
    # password += random_alphabet
    password_list.append(random.choice(alphabet))
    
for char in range(1, nr_symbol + 1):
    password_list += random.choice(symbol)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password_string = ""
for char in password_list:
    password_string += char
    
print(f"Your password is {password_string} ")