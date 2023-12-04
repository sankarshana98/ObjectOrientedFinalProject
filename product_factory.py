from product import Electronics, Clothing, Shoes, BeautyProduct, generate_id

class ProductFactory:
    def create_product(self, category, *args, **kwargs):
        product_id = generate_id()  # Generate a unique ID for the product
        if category == "Electronics":
            return Electronics(product_id, *args, **kwargs)
        elif category == "Clothing":
            return Clothing(product_id, *args, **kwargs)
        elif category == "Shoes":
            return Shoes(product_id, *args, **kwargs)
        elif category == "Beauty":
            return BeautyProduct(product_id, *args, **kwargs)
        else:
            raise ValueError("Invalid category")

    def serialize(self, product):
        return product.serialize()