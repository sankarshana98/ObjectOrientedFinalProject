from random import choice

class RecommendationSystem:
    def __init__(self, all_products):
        self.all_products = all_products

    def get_similar_items(self, selected_product, num_recommendations=3):
        similar_items = [product for product in self.all_products if type(product) == type(selected_product) and product != selected_product]

        # Ensure the number of recommendations does not exceed the available similar items
        num_recommendations = min(num_recommendations, len(similar_items))

        return [choice(similar_items) for _ in range(num_recommendations)] if similar_items else []
