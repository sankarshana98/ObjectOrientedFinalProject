from generateId import generate_id

class Product:
    def __init__(self, product_id, name, price, description, rating):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}\nPrice: ${self.price}\nDescription: {self.description}\nRating: {self.rating}")

    def serialize(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'rating': self.rating
        }

# Update subclasses to include product_id
class Electronics(Product):
    def __init__(self, product_id, name, price, description, rating, brand):
        super().__init__(product_id, name, price, description, rating)
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")

class Clothing(Product):
    def __init__(self, product_id, name, price, description, rating, size):
        super().__init__(product_id, name, price, description, rating)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

class Shoes(Product):
    def __init__(self, product_id, name, price, description, rating, size):
        super().__init__(product_id, name, price, description, rating)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

class BeautyProduct(Product):
    def __init__(self, product_id, name, price, description, rating, brand):
        super().__init__(product_id, name, price, description, rating)
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
