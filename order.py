import json
from product import Product
from generateId import generate_id


class Orders:
    def __init__(self):
        self.orders = []

    def add_order(self, user_id, products):
        order = {
            'order_id': generate_id(),
            'user_id': user_id,
            'products': [product.serialize() for product in products],
            'total_price': sum(product.price for product in products)
        }
        self.orders.append(order)
        self.save_to_file()

    def get_orders_by_user(self, user_id):
        user_orders = [order for order in self.orders if order['user_id'] == user_id]
        return user_orders

    def save_to_file(self):
        with open('orders.json', 'w') as file:
            json.dump(self.orders, file)

    def load_from_file(self):
        try:
            with open('orders.json', 'r') as file:
                self.orders = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize with an empty list
            self.orders = []

