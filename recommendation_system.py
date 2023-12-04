class RecommendationSystem:
    def __init__(self, all_products):
        self.all_products = all_products

    def get_recommendations(self, product_id, num_recommendations=8):
        # Replace this simple recommendation logic with your own algorithm
        product = self.find_product_by_id(product_id)
        if product:
            category = product.category
            recommendations = []

            for other_product in self.all_products.get(category, []):
                if other_product.product_id != product_id:
                    recommendations.append(other_product)

            # # Sort recommendations by rating (you can customize this)
            recommendations.sort(key=lambda p: p.rating, reverse=True)

            return recommendations[:num_recommendations]

        return []

    def find_product_by_id(self, product_id):
        for category, products in self.all_products.items():
            for product in products:
                if product.product_id == product_id:
                    return product
        return None