from product import Electronics, Clothing, Shoes, BeautyProduct, generate_id

class ProductFactory:
    def __init__(self):
        """
        Initialize a ProductFactory instance.

        Attributes:
        - product_counter (int): Counter to keep track of the generated product IDs.
        """
        self.product_counter = 1 

    def create_product(self, category, *args, **kwargs):
        """
        Create a product based on the given category.

        Parameters:
        - category (str): The category of the product to be created.
        - *args: Positional arguments passed to the product constructor.
        - **kwargs: Keyword arguments passed to the product constructor.

        Returns:
        - Product: An instance of the created product.

        Raises:
        - ValueError: If an invalid category is provided.
        """
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
        """
        Serialize product information into a dictionary.

        Parameters:
        - product (Product): The product to be serialized.

        Returns:
        - dict: A dictionary containing product information.
        """
        return product.serialize()
