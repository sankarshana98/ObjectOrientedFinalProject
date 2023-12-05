from typing import List

class RecommendationStrategy:
    def get_recommendations(self, product_id, all_products, num_recommendations):
        """
        Abstract method to be implemented by subclasses.
        Gets product recommendations based on a specific strategy.

        Parameters:
        - product_id: The ID of the product for which recommendations are requested.
        - all_products (dict): A dictionary containing all products, organized by category.
        - num_recommendations (int): The number of recommendations to retrieve.

        Returns:
        - list: A list of recommended products.
        """
        raise NotImplementedError("Subclasses must implement this method")



from recommendation_strategy import RecommendationStrategy

class SameCategoryRecommendation(RecommendationStrategy):
    def get_recommendations(self, product_id, all_products, num_recommendations):
        """
        Implementation of the recommendation strategy that recommends products from the same category.

        Parameters:
        - product_id: The ID of the product for which recommendations are requested.
        - all_products (dict): A dictionary containing all products, organized by category.
        - num_recommendations (int): The number of recommendations to retrieve.

        Returns:
        - list: A list of recommended products.
        """
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
        """
        Helper method to find a product by ID in the provided dictionary of all products.

        Parameters:
        - product_id: The ID of the product to find.
        - all_products (dict): A dictionary containing all products, organized by category.

        Returns:
        - Product or None: The found product or None if not found.
        """
        for category, products in all_products.items():
            for product in products:
                if product.product_id == product_id:
                    return product
        return None


class HistoryBasedRecommendationStrategy(RecommendationStrategy):
    def get_recommendations(self, product_id, all_products, num_recommendations, user_id):
        """
        Implementation of a history-based recommendation strategy.

        Parameters:
        - product_id: The ID of the product for which recommendations are requested.
        - all_products (dict): A dictionary containing all products, organized by category.
        - num_recommendations (int): The number of recommendations to retrieve.
        - user_id: The ID of the user for whom the recommendations are generated based on history.

        Returns:
        - list: A list of recommended products.
        """
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
        """
        Helper method to find a product by ID in the provided dictionary of all products.

        Parameters:
        - product_id: The ID of the product to find.
        - all_products (dict): A dictionary containing all products, organized by category.

        Returns:
        - Product or None: The found product or None if not found.
        """
        for category, products in all_products.items():
            for product in products:
                if product.product_id == product_id:
                    return product
        return None
