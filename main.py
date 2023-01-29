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
