from flask import Flask, render_template, request, redirect, url_for, session
from authentication import AuthSingleton
from user_login import LoginCommand, LogoutCommand, Invoker
from produc_main import get_all_products, get_product_details
from generateId import generate_id
from get_orders_by_user import get_orders_by_user_id
from get_userId import get_user_id_by_username
from flask import redirect
import json
from recommendation_system import RecommendationSystem
from recommendation_strategy import RecommendationStrategy, SameCategoryRecommendation, HistoryBasedRecommendationStrategy

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 
auth_instance = AuthSingleton()
invoker = Invoker()

# Home route
@app.route('/')
def home():
    # Get the logged-in user
    logged_in_user = auth_instance.get_logged_in_user()
    # Display a welcome message if a user is logged in
    welcome_message = f"Welcome, {logged_in_user['username']}!" if logged_in_user else None
    return render_template('index.html', logged_in_user=logged_in_user, welcome_message=welcome_message)

# Route for creating a new user
@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        # Retrieve user details from the form
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        email = request.form['email']

        # Check if a profile picture is uploaded
        if 'profile_pic' in request.files:
            profile_pic = request.files['profile_pic']
            profile_pic_filename = profile_pic.filename
        else:
            profile_pic_filename = None

        # Create a new user using the authentication singleton
        auth_instance.create_user(username, password, full_name, email, profile_pic_filename)
        # Redirect to the home page after successful user creation
        return redirect(url_for('home'))

    return render_template('create_user.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve username and password from the login form
        username = request.form['username']
        password = request.form['password']

        # Check if the provided credentials are valid
        if auth_instance.login(username, password):
            # If valid, store the username in the session and redirect to the dashboard
            session['current_username'] = username 
            return redirect(url_for('dashboard'))  
        else:
            # If invalid, display an error message
            error_message = "Incorrect username or password. Please try again."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

# Route for product information
@app.route('/product_info', methods=['GET', 'POST'])
def product_info():
    if request.method == 'POST':
        # Handle the case when a user adds items to the cart and proceeds to checkout
        cart = request.json.get('cart')
        if cart:
            user_id = auth_instance.get_logged_in_user()['user_id']
            total_price = sum(product['price'] for product in cart)
            order_id = generate_id()  
            order_data = {
                'order_id': order_id,
                'user_id': user_id,
                'products': cart,
                'total_price': total_price
            }

            # Save the order details to a file (you may want to use a database)
            with open('orders.json', 'a') as file:
                json.dump(order_data, file, indent=2)
                file.write('\n')

            # Redirect to the previous orders page
            return redirect(url_for('previous_orders'))

    # Retrieve information for displaying products and recommendations
    logged_in_user = auth_instance.get_logged_in_user()
    all_products = get_all_products()
    selected_category = request.args.get('category', None)
    order_history = get_orders_by_user_id(logged_in_user['user_id'])

    # Create a recommendation system and get product recommendations
    recommendation_system = RecommendationSystem(all_products)
    recommendations = recommendation_system.get_recommendations(product_id=None, order_history=order_history)

    # Render the product information page with the retrieved data
    return render_template('product_info.html', all_products=all_products, selected_category=selected_category, recommendations=recommendations)    

# Route for user logout
@app.route('/logout')
def logout():
    # Create a logout command, set it in the invoker, and execute the command
    logout_command = LogoutCommand(auth_instance)
    invoker.set_command(logout_command)
    invoker.execute_command()
    # Redirect to the home page after logout
    return redirect(url_for('home'))

# Route for handling the checkout process
@app.route('/product', methods=['GET'])
def product():
    if request.method == 'POST':
        # Handle the case when a user adds items to the cart and proceeds to checkout
        cart = request.json.get('cart')
        if cart:
            user_id = auth_instance.get_logged_in_user()['user_id']
            total_price = sum(product['price'] for product in cart)
            order_id = generate_id()  
            order_data = {
                'order_id': order_id,
                'user_id': user_id,
                'products': cart,
                'total_price': total_price
            }

            # Save the order details to a file (you may want to use a database)
            with open('orders.json', 'a') as file:
                json.dump(order_data, file, indent=2)
                file.write('\n')

            # Redirect to the previous orders page
            return redirect(url_for('previous_orders'))

    # Retrieve information for displaying products and recommendations
    logged_in_user = auth_instance.get_logged_in_user()
    all_products = get_all_products()
    selected_category = request.args.get('category', None)

    # Create a recommendation system and get product recommendations based on history
    recommendation_system = RecommendationSystem(all_products)
    history_based_strategy = HistoryBasedRecommendationStrategy()
    recommendations_history_based = recommendation_system.get_recommendations(123, history_based_strategy, get_user_id())

    # Render the product information page with the retrieved data
    return render_template('product_info.html', all_products=all_products, selected_category=selected_category,
                           history_based_strategy=recommendations_history_based)

# Route for the user dashboard
@app.route('/dashboard')
def dashboard():
    # Retrieve the logged-in user
    logged_in_user = auth_instance.get_logged_in_user()

    # Redirect to the login page if no user is logged in
    if not logged_in_user:
        return redirect(url_for('login'))

    # Retrieve information for displaying products on the dashboard
    all_products = get_all_products()

    # Render the dashboard page with the retrieved data
    return render_template('dashboard.html', logged_in_user=logged_in_user, all_products=all_products)

# Route for displaying products by category
@app.route('/product_by_category/<category>', methods=['GET'])
def product_by_category(category):
    # Retrieve information for displaying products by category
    all_products = get_all_products()
    
    # Render the product information page with the retrieved data and selected category
    return render_template('product_info.html', all_products=all_products, selected_category=category)

# Route for viewing the user profile
@app.route('/view_profile')
def view_profile():
    # Retrieve the logged-in user and information for displaying products
    logged_in_user = auth_instance.get_logged_in_user()
    all_products = get_all_products()  

    # Render the user profile page with the retrieved data
    return render_template('view_profile.html', logged_in_user=logged_in_user, all_products=all_products)

# Route for updating the user profile
@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    # Retrieve the logged-in user
    logged_in_user = auth_instance.get_logged_in_user()

    if request.method == 'POST':
        # Update user profile based on the form data
        updated_full_name = request.form.get('full_name')
        updated_email = request.form.get('email')

        logged_in_user['full_name'] = updated_full_name
        logged_in_user['email'] = updated_email

        # Print a message indicating that the user profile has been updated
        print(f"User profile updated: {logged_in_user}")

        # Redirect to the user profile page after the update
        return redirect(url_for('view_profile'))

    # Render the update profile page with the retrieved user data
    return render_template('update_profile.html', logged_in_user=logged_in_user)

# Route for displaying all products
@app.route('/products')
def products():
    # Retrieve information for displaying all products
    all_products = get_all_products()

    # Render the product information page with the retrieved data
    return render_template('product_info.html', all_products=all_products)

# Route for displaying detailed information about a specific product
@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Retrieve all product data
    all_products_data = get_all_products()
    # Retrieve details for the specific product
    product_details = get_product_details(product_id, all_products_data)

    # Check if the product details are available
    if product_details:
        # Create a recommendation system using the same category strategy
        same_category_strategy = SameCategoryRecommendation()
        recommendation_system = RecommendationSystem(all_products_data, same_category_strategy)
        # Get product recommendations based on the same category
        recommendations = recommendation_system.get_recommendations(product_id)
        # Render the product details page with the retrieved data and recommendations
        return render_template('product_details.html', product_details=product_details, recommendations=recommendations)
    else:
        # Display a message if the product is not found
        return "Product not found"

# Route for displaying previous orders of the user
@app.route('/previous_orders')
def previous_orders():
    # Print the content of the session for debugging purposes
    print(f"Session Content: {session}")
    # Retrieve the user ID based on the current username stored in the session
    user_id = get_user_id_by_username(session['current_username'])
    # Print the current user ID for debugging purposes
    print(f"Current User ID: {user_id}")
    # Retrieve the orders for the user based on the user ID
    orders = get_orders_by_user_id(user_id)
    # Print the retrieved orders for debugging purposes
    print(f"Orders: {orders}")
    # Render the previous orders page with the retrieved order data
    return render_template('previous_orders.html', orders=orders)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
