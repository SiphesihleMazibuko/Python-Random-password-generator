import random

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "`!@#$%^&*()_+=-~{}[]';/?><,"
password = " "
combination = lowerCase + upperCase + numbers + symbols
length = int(input('Enter the length of your password: '))

for i in range(length):
    password += random.choice(combination)
print(password)
