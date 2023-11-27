from product import Electronics, Clothing, Shoes, BeautyProduct

class ProductFactory:
    def create_product(self, category, *args, **kwargs):
        if category == "Electronics":
            return Electronics(*args, **kwargs)
        elif category == "Clothing":
            return Clothing(*args, **kwargs)
        elif category == "Shoes":
            return Shoes(*args, **kwargs)
        elif category == "Beauty":
            return BeautyProduct(*args, **kwargs)
        else:
            raise ValueError("Invalid category")
