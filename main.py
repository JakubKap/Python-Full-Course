import os.path
from datetime import datetime

import calculator
from phone import Phone

# calculator operations
print("Calculator operations results:")
print(calculator.add(2, 2))
print(calculator.subtract(2, 2))
print(calculator.divide(2, 2))
print(calculator.multiply(2, 3))

# Phone operations
iphone = Phone("IPhone 7+", 300)
samsung = Phone("Samsung S20", 1400)

print("\nPhone creations results:")
print(iphone)
print(samsung)

# Working with dates
print("\nDates examples:")
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

# Date formatting
print("\nFormatted date:")
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))

# File operations (w - writing, a - appending, r+ - reading and writing)
filename = "./data.csv"
file = open(filename, "w")
file.write("id, name, email\n")
file.write("1, Jakub, jk@gmail.com\n")
file.write("2, John, john@gmail.com\n")
file.close()

print("\nFile content:")
file = open(filename, "r")
for line in file:
    print(line)
file.close()

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"File {filename} does not exist")
