from flask import Flask, render_template, request, redirect, url_for
from authentication import AuthSingleton
from user_login import LoginCommand, LogoutCommand, Invoker
from flask import redirect
from product_main import get_all_products, get_product_details
from generateId import generate_id
from get_orders_by_user import get_orders_by_user_id
from get_userId import get_user_id_by_username
from flask import session
import json
from recommendation_system import RecommendationSystem
from recommendation_strategy import RecommendationStrategy, SameCategoryRecommendation, HistoryBasedRecommendationStrategy
from observer import VisitCounter
from notification_observer import NotificationObserver


app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 
auth_instance = AuthSingleton()
invoker = Invoker()


notification_count = 0

visitCounter = VisitCounter()
notification_observer = NotificationObserver()
visitCounter.attach(notification_observer)

# Home route
@app.route('/')
def home():
    logged_in_user = auth_instance.get_logged_in_user()
    welcome_message = f"Welcome, {logged_in_user['username']}!" if logged_in_user else None
    return render_template('index.html', logged_in_user=logged_in_user, welcome_message=welcome_message)


@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    """
    Creating new USER
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        email = request.form['email']

        # Handle profile picture upload
        if 'profile_pic' in request.files:
            profile_pic = request.files['profile_pic']
            profile_pic_filename = profile_pic.filename
        else:
            profile_pic_filename = None

        auth_instance.create_user(username, password, full_name, email, profile_pic_filename)
        return redirect(url_for('home'))

    return render_template('create_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login the USER
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if auth_instance.login(username, password):
            session['current_username'] = username 
            return redirect(url_for('dashboard'))  
        else:
            error_message = "Incorrect username or password. Please try again."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/product_info', methods=['GET', 'POST'])
def product_info():
    """
    Show products information
    """
    if request.method == 'POST':
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

            with open('orders.json', 'a') as file:
                json.dump(order_data, file, indent=2)
                file.write('\n')

            return redirect(url_for('previous_orders'))

    logged_in_user = auth_instance.get_logged_in_user()
    all_products = get_all_products()
    selected_category = request.args.get('category', None)
    order_history = get_orders_by_user_id(logged_in_user['user_id'])

    recommendation_system = RecommendationSystem(all_products)
    recommendations = recommendation_system.get_recommendations(product_id=None, order_history=order_history)

    return render_template('product_info.html', all_products=all_products, selected_category=selected_category, recommendations=recommendations)    # logged_in_user = auth_instance.get_logged_in_user()
    
@app.route('/logout')
def logout():
    """
    USER logout
    """
    logout_command = LogoutCommand(auth_instance)
    invoker.set_command(logout_command)
    invoker.execute_command()
    return redirect(url_for('home'))

@app.route('/product', methods=['GET'])
def product():
    """
    Shoe recommendations based on products
    """
    if request.method == 'POST':
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

            with open('orders.json', 'a') as file:
                json.dump(order_data, file, indent=2)
                file.write('\n')

            return redirect(url_for('previous_orders'))

    logged_in_user = auth_instance.get_logged_in_user()
    all_products = get_all_products()
    selected_category = request.args.get('category', None)

    recommendation_system = RecommendationSystem(all_products)
    history_based_strategy = HistoryBasedRecommendationStrategy()
    recommendations_history_based = recommendation_system.get_recommendations(123, history_based_strategy, get_user_id_by_username(session['current_username']))

    return render_template('product_info.html', all_products=all_products, selected_category=selected_category,
                           history_based_strategy=recommendations_history_based)

@app.route('/dashboard')
def dashboard():
    """
    Go to main dashboard
    """
    logged_in_user = auth_instance.get_logged_in_user()

    if not logged_in_user:
        return redirect(url_for('login'))

    all_products = get_all_products()
    return render_template('dashboard.html', logged_in_user=logged_in_user, all_products=all_products)

@app.route('/product_by_category/<category>', methods=['GET'])
def product_by_category(category):
    """
    Display products based on category
    """
    all_products = get_all_products()
    
    return render_template('product_info.html', all_products=all_products, selected_category=category)

@app.route('/view_profile')
def view_profile():
    """
    Show user profile
    """
    logged_in_user = auth_instance.get_logged_in_user()
    all_products = get_all_products()  
    return render_template('view_profile.html', logged_in_user=logged_in_user, all_products=all_products)

@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    """
    Update user profile
    """
    logged_in_user = auth_instance.get_logged_in_user()

    if request.method == 'POST':
        updated_full_name = request.form.get('full_name')
        updated_email = request.form.get('email')

        logged_in_user['full_name'] = updated_full_name
        logged_in_user['email'] = updated_email

        print(f"User profile updated: {logged_in_user}")

        return redirect(url_for('view_profile'))

    return render_template('update_profile.html', logged_in_user=logged_in_user)

@app.route('/products')
def products():
    all_products = get_all_products()
    return render_template('product_info.html', all_products=all_products)
@app.route('/product/<int:product_id>')
def product_details(product_id):
    """
    Show product details and get notification of new recommendations
    """
    visitCounter.increment_counter()
    all_products_data = get_all_products()
    product_details = get_product_details(product_id, all_products_data)

    if visitCounter.counter % 3 == 0:
        notification_observer.update("You have new recommendations!")
        global notification_count
        notification_count += 1
    
    if product_details:
        same_category_strategy = SameCategoryRecommendation()
        recommendation_system = RecommendationSystem(all_products_data, same_category_strategy)
        recommendations = recommendation_system.get_recommendations(product_id)

        return render_template('product_details.html', product_details=product_details, recommendations=recommendations, notification_count=notification_count)
    else:
        return "Product not found"
@app.route('/previous_orders')
def previous_orders():
    """
    Show previous order data
    """
    print(f"Session Content: {session}")
    user_id = get_user_id_by_username(session['current_username'])
    print(f"Current User ID: {user_id}")
    orders = get_orders_by_user_id(user_id)
    print(f"Orders: {orders}")
    return render_template('previous_orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)