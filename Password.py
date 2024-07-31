import random

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "`!@#$%^&*()_+=-~{}[]';/?><,"
password = " "

letters = int(input('Enter the letters would you like in your password?\n'))
symbols_ = int(input('How many symbols would you like?\n'))
nums = int(input('How many numbers would you like?\n'))

password_characters = []

for i in range(letters):
    password_characters.append(random.choice(lowerCase + upperCase))

for i in range(symbols_):
    password_characters.append(random.choice(symbols))

for i in range(nums):
    password_characters.append(random.choice(numbers))

random.shuffle(password_characters)

password = ''.join(password_characters)

print('Here is your password:',password)



