import random
from utils import *
    
print("Welcome to password generator!")
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))

password = []

for i in range(0, no_of_letters):
    password.append(random.choice(letters))

for i in range(0, no_of_numbers):
    password.append(random.choice(numbers))
    
for i in range(0, no_of_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
print(''.join(password))
