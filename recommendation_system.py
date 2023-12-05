from recommendation_strategy import RecommendationStrategy

class RecommendationSystem:
    def __init__(self, all_products, recommendation_strategy: RecommendationStrategy):
        """
        Initialize a RecommendationSystem.

        Parameters:
        - all_products (dict): A dictionary containing all products, organized by category.
        - recommendation_strategy (RecommendationStrategy): An instance of a recommendation strategy.

        Note:
        - The `all_products` dictionary should have categories as keys, and values as lists of products
          belonging to that category.
        - The `recommendation_strategy` is an object that defines the strategy for generating recommendations.
        """
        self.all_products = all_products
        self.recommendation_strategy = recommendation_strategy
        self.observers = []  # List to store observers (if any)

    def get_recommendations(self, product_id, num_recommendations=8):
        """
        Get product recommendations based on the set recommendation strategy.

        Parameters:
        - product_id: The ID of the product for which recommendations are requested.
        - num_recommendations (int): The number of recommendations to retrieve (default is 8).

        Returns:
        - list: A list of recommended products.
        """
        return self.recommendation_strategy.get_recommendations(product_id, self.all_products, num_recommendations)
