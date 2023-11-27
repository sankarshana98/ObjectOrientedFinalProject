from random import randint
from product import Electronics, Clothing, Shoes, BeautyProduct
from product_factory import ProductFactory
from recommendation_system import RecommendationSystem
from user import User
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

    # user1 = User("User1")
    # product_management_system.add_observer(user1)

    recommendation_system = RecommendationSystem(all_products)

    similar_items = recommendation_system.get_similar_items(selected_product, num_recommendations=3)
    if similar_items:
        print("\nRecommended Similar Products:")
        for idx, similar_item in enumerate(similar_items, start=1):
            print(f"{idx}. {similar_item.name}")
            similar_item.display_info()
            print("\n")
    else:
        print("\nNo similar items found in the same category.")

    # new_beauty_product = product_factory.create_product("Beauty", f"New Lip Gloss_{randint(1, 100)}", 24.99, "Shiny lip gloss", 4.5, "PQR Cosmetics")
    # product_management_system.add_product(new_beauty_product)

if __name__ == "__main__":
    main()