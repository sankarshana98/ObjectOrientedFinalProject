class Product:
    def __init__(self, name, price, description, rating):
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating

    def display_info(self):
        print(f"Name: {self.name}\nPrice: ${self.price}\nDescription: {self.description}\nRating: {self.rating}")

class Electronics(Product):
    def __init__(self, name, price, description, rating, brand):
        super().__init__(name, price, description, rating)
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")

class Clothing(Product):
    def __init__(self, name, price, description, rating, size):
        super().__init__(name, price, description, rating)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

class Shoes(Product):
    def __init__(self, name, price, description, rating, size):
        super().__init__(name, price, description, rating)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

class BeautyProduct(Product):
    def __init__(self, name, price, description, rating, brand):
        super().__init__(name, price, description, rating)
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
