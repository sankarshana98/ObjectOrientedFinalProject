import json
from product import Product
from generateId import generate_id


class Orders:
    def __init__(self):
        """
        Initialize an Orders instance.

        Attributes:
        - orders (list): A list to store order information.
        """
        self.orders = []

    def add_order(self, user_id, products):
        """
        Add a new order to the orders list.

        Parameters:
        - user_id (str): The user ID associated with the order.
        - products (list): A list of Product instances representing the products in the order.
        """
        order = {
            'order_id': generate_id(),
            'user_id': user_id,
            'products': [product.serialize() for product in products],
            'total_price': sum(product.price for product in products)
        }
        self.orders.append(order)
        self.save_to_file()

    def get_orders_by_user(self, user_id):
        """
        Get all orders associated with a specific user.

        Parameters:
        - user_id (str): The user ID for which orders are requested.

        Returns:
        - list: A list of orders associated with the specified user.
        """
        user_orders = [order for order in self.orders if order['user_id'] == user_id]
        return user_orders

    def save_to_file(self):
        """
        Save the orders information to a JSON file.
        """
        with open('orders.json', 'w') as file:
            json.dump(self.orders, file)

    def load_from_file(self):
        """
        Load orders information from a JSON file, if it exists.
        If the file doesn't exist, initialize the orders list with an empty list.
        """
        try:
            with open('orders.json', 'r') as file:
                self.orders = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with an empty list
            self.orders = []
