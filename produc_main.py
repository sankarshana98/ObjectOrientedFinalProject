# main.py
from random import randint
from product import Electronics, Clothing, Shoes, BeautyProduct
from product_factory import ProductFactory
from product_management_system import ProductManagementSystem

def main():
    product_factory = ProductFactory()
    product_management_system = ProductManagementSystem([])

    all_products = []

    for _ in range(5):
        laptop = product_factory.create_product("Electronics", f"Laptop_{randint(1, 100)}", 999.99, "High-performance laptop", 4.5, "ABC Electronics")
        t_shirt = product_factory.create_product("Clothing", f"T-shirt_{randint(1, 100)}", 19.99, "Comfortable cotton T-shirt", 4.0, "M")
        running_shoes = product_factory.create_product("Shoes", f"Running Shoes_{randint(1, 100)}", 79.99, "Durable running shoes", 4.2, "10")
        lipstick = product_factory.create_product("Beauty", f"Lipstick_{randint(1, 100)}", 14.99, "Long-lasting lipstick", 4.8, "XYZ Cosmetics")

        all_products.extend([laptop, t_shirt, running_shoes, lipstick])

    print("All Products:")
    for idx, product in enumerate(all_products, start=1):
        print(f"{idx}. {product.name}")

    selected_index = int(input("Select a product (enter the number): ")) - 1

    selected_product = all_products[selected_index]
    print("\nSelected Product:")
    selected_product.display_info()



if __name__ == "__main__":
    main()
