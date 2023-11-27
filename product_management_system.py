from observer import ProductSubject

class ProductManagementSystem(ProductSubject):
    def __init__(self, all_products):
        super().__init__()
        self.all_products = all_products

    def add_product(self, product):
        self.all_products.append(product)
        self.notify_observers(f"New product added: {product.name}")