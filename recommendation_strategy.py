from typing import List

class RecommendationStrategy:
    def get_recommendations(self, product_id, all_products, num_recommendations):
        raise NotImplementedError("Subclasses must implement this method")
    
# same_category_recommendation.py

from recommendation_strategy import RecommendationStrategy

class SameCategoryRecommendation(RecommendationStrategy):
    def get_recommendations(self, product_id, all_products, num_recommendations):
        product = self.find_product_by_id(product_id, all_products)
        if product:
            category = product.category
            recommendations = []

            for other_product in all_products.get(category, []):
                if other_product.product_id != product_id:
                    recommendations.append(other_product)

            # Sort recommendations by rating (you can customize this)
            recommendations.sort(key=lambda p: p.rating, reverse=True)

            return recommendations[:num_recommendations]

        return []

    def find_product_by_id(self, product_id, all_products):
        for category, products in all_products.items():
            for product in products:
                if product.product_id == product_id:
                    return product
        return None


class HistoryBasedRecommendationStrategy(RecommendationStrategy):
    def get_recommendations(self, product_id, all_products, num_recommendations, user_id):
        product = self.find_product_by_id(product_id, all_products)
        if product:
            category = product.category
            recommendations = []

            for other_product in all_products.get(category, []):
                if other_product.product_id != product_id:
                    recommendations.append(other_product)

            recommendations.sort(key=lambda p: p.rating, reverse=True)

            return recommendations[:num_recommendations]

        return []

    def find_product_by_id(self, product_id, all_products):
        for category, products in all_products.items():
            for product in products:
                if product.product_id == product_id:
                    return product
        return None
