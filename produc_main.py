# main.py
from random import randint
from product import Electronics, Clothing, Shoes, BeautyProduct
from product_factory import ProductFactory
# from product_management_system import ProductManagementSystem

# def main():
#     product_factory = ProductFactory()
#     # product_management_system = ProductManagementSystem([])

#     all_products = []

#     for _ in range(5):
#         laptop = product_factory.create_product("Electronics", f"Laptop_{randint(1, 100)}", 999.99, "High-performance laptop", 4.5, "ABC Electronics")
#         t_shirt = product_factory.create_product("Clothing", f"T-shirt_{randint(1, 100)}", 19.99, "Comfortable cotton T-shirt", 4.0, "M")
#         running_shoes = product_factory.create_product("Shoes", f"Running Shoes_{randint(1, 100)}", 79.99, "Durable running shoes", 4.2, "10")
#         lipstick = product_factory.create_product("Beauty", f"Lipstick_{randint(1, 100)}", 14.99, "Long-lasting lipstick", 4.8, "XYZ Cosmetics")

#         all_products.extend([laptop, t_shirt, running_shoes, lipstick])

#     print("All Products:")
#     for idx, product in enumerate(all_products, start=1):
#         print(f"{idx}. {product.name}")

#     selected_index = int(input("Select a product (enter the number): ")) - 1

#     selected_product = all_products[selected_index]
#     print("\nSelected Product:")
#     selected_product.display_info()

# if __name__ == "__main__":
#     main()

def get_selected_product(index):
    product_factory = ProductFactory()
    all_products = []

    for _ in range(5):
        laptop = product_factory.create_product("Electronics", f"Laptop_{randint(1, 100)}", 999.99, "High-performance laptop", 4.5, "ABC Electronics")
        t_shirt = product_factory.create_product("Clothing", f"T-shirt_{randint(1, 100)}", 19.99, "Comfortable cotton T-shirt", 4.0, "M")
        running_shoes = product_factory.create_product("Shoes", f"Running Shoes_{randint(1, 100)}", 79.99, "Durable running shoes", 4.2, "10")
        lipstick = product_factory.create_product("Beauty", f"Lipstick_{randint(1, 100)}", 14.99, "Long-lasting lipstick", 4.8, "XYZ Cosmetics")

        all_products.extend([laptop, t_shirt, running_shoes, lipstick])

    return all_products[index]

def get_all_products():
    product_factory = ProductFactory()
    all_products = {"Electronics": [], "Clothing": [], "Shoes": [], "Beauty": []}

    for _ in range(5):
        laptop = product_factory.create_product("Electronics", f"Laptop_{randint(1, 100)}", 999.99, "High-performance laptop", 4.5, "ABC Electronics")
        t_shirt = product_factory.create_product("Clothing", f"T-shirt_{randint(1, 100)}", 19.99, "Comfortable cotton T-shirt", 4.0, "M")
        running_shoes = product_factory.create_product("Shoes", f"Running Shoes_{randint(1, 100)}", 79.99, "Durable running shoes", 4.2, "10")
        lipstick = product_factory.create_product("Beauty", f"Lipstick_{randint(1, 100)}", 14.99, "Long-lasting lipstick", 4.8, "XYZ Cosmetics")

        all_products["Electronics"].append(laptop)
        all_products["Clothing"].append(t_shirt)
        all_products["Shoes"].append(running_shoes)
        all_products["Beauty"].append(lipstick)

    return all_products

def get_product_details(product_id, all_products):
    for category, products in all_products.items():
        for product in products:
            if product.product_id == product_id:
                product_details = {
                    "product_id": product.product_id,
                    "name": product.name,
                    "price": product.price,
                    "description": product.description,
                    "rating": product.rating,
                }
                # Handle category-specific attributes
                if isinstance(product, Electronics):
                    product_details["brand"] = product.brand
                elif isinstance(product, Clothing):
                    product_details["size"] = product.size
                elif isinstance(product, Shoes):
                    product_details["size"] = product.size
                elif isinstance(product, BeautyProduct):
                    product_details["brand"] = product.brand

                return product_details
    return None
