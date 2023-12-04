from product import Electronics, Clothing, Shoes, BeautyProduct, generate_id

class ProductFactory:
    def __init__(self):
        self.product_counter = 1 
    def create_product(self, category, *args, **kwargs):
        product_id = self.product_counter
        self.product_counter += 1
        if category == "Electronics":
            return Electronics(product_id, category, *args, **kwargs)
        elif category == "Clothing":
            return Clothing(product_id, category, *args, **kwargs)
        elif category == "Shoes":
            return Shoes(product_id, category, *args, **kwargs)
        elif category == "Beauty":
            return BeautyProduct(product_id, category, *args, **kwargs)
        else:
            raise ValueError("Invalid category")

    def serialize(self, product):
        return product.serialize()