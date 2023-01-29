class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Price: {self.price}"


