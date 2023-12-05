from generateId import generate_id

class Product:
    def __init__(self, product_id, category, name, price, description, rating):
        """
        Initialize a Product instance.

        Parameters:
        - product_id (str): The unique identifier for the product.
        - category (str): The category to which the product belongs.
        - name (str): The name of the product.
        - price (float): The price of the product.
        - description (str): The description of the product.
        - rating (float): The rating of the product.
        """
        self.product_id = product_id
        self.category = category
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating

    def display_info(self):
        """
        Display information about the product.
        """
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}\nPrice: ${self.price}\nDescription: {self.description}\nRating: {self.rating}")

    def serialize(self):
        """
        Serialize the product information into a dictionary.

        Returns:
        - dict: A dictionary containing product information.
        """
        return {
            'product_id': self.product_id,
            'category': self.category,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'rating': self.rating
        }


class Electronics(Product):
    def __init__(self, product_id, category, name, price, description, rating, brand):
        """
        Initialize an Electronics instance.

        Parameters:
        - product_id (str): The unique identifier for the product.
        - category (str): The category to which the product belongs.
        - name (str): The name of the product.
        - price (float): The price of the product.
        - description (str): The description of the product.
        - rating (float): The rating of the product.
        - brand (str): The brand of the electronics product.
        """
        super().__init__(product_id, category, name, price, description, rating)
        self.brand = brand

    def display_info(self):
        """
        Display information about the electronics product.
        """
        super().display_info()
        print(f"Brand: {self.brand}")


class Clothing(Product):
    def __init__(self, product_id, category, name, price, description, rating, size):
        """
        Initialize a Clothing instance.

        Parameters:
        - product_id (str): The unique identifier for the product.
        - category (str): The category to which the product belongs.
        - name (str): The name of the product.
        - price (float): The price of the product.
        - description (str): The description of the product.
        - rating (float): The rating of the product.
        - size (str): The size of the clothing product.
        """
        super().__init__(product_id, category, name, price, description, rating)
        self.size = size

    def display_info(self):
        """
        Display information about the clothing product.
        """
        super().display_info()
        print(f"Size: {self.size}")


class Shoes(Product):
    def __init__(self, product_id, category, name, price, description, rating, size):
        """
        Initialize a Shoes instance.

        Parameters:
        - product_id (str): The unique identifier for the product.
        - category (str): The category to which the product belongs.
        - name (str): The name of the product.
        - price (float): The price of the product.
        - description (str): The description of the product.
        - rating (float): The rating of the product.
        - size (str): The size of the shoes product.
        """
        super().__init__(product_id, category, name, price, description, rating)
        self.size = size

    def display_info(self):
        """
        Display information about the shoes product.
        """
        super().display_info()
        print(f"Size: {self.size}")


class BeautyProduct(Product):
    def __init__(self, product_id, category, name, price, description, rating, brand):
        """
        Initialize a BeautyProduct instance.

        Parameters:
        - product_id (str): The unique identifier for the product.
        - category (str): The category to which the product belongs.
        - name (str): The name of the product.
        - price (float): The price of the product.
        - description (str): The description of the product.
        - rating (float): The rating of the product.
        - brand (str): The brand of the beauty product.
        """
        super().__init__(product_id, category, name, price, description, rating)
        self.brand = brand

    def display_info(self):
        """
        Display information about the beauty product.
        """
        super().display_info()
        print(f"Brand: {self.brand}")