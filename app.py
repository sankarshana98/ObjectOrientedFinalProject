from flask import Flask, render_template, request, redirect, url_for
from authentication import AuthSingleton
from user_login import LoginCommand, LogoutCommand, Invoker
from flask import redirect
from produc_main import get_all_products, get_selected_product

app = Flask(__name__)
auth_instance = AuthSingleton()
invoker = Invoker()


@app.route('/')
def home():
    logged_in_user = auth_instance.get_logged_in_user()
    return render_template('index.html', logged_in_user=logged_in_user)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        auth_instance.create_user(username, password)
        return redirect(url_for('home'))
    return render_template('create_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        login_command = LoginCommand(auth_instance, username, password)
        invoker.set_command(login_command)
        invoker.execute_command()
        
        # Check if the login was successful
        if auth_instance.get_logged_in_user():
            return redirect(url_for('product'))  # Redirect to /product after successful login
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_command = LogoutCommand(auth_instance)
    invoker.set_command(logout_command)
    invoker.execute_command()
    return redirect(url_for('home'))

@app.route('/product', methods=['GET'])
def product():
    all_products = get_all_products()
    selected_category = request.args.get('category', None)
    return render_template('product_info.html', all_products=all_products, selected_category=selected_category)

# Add a route for displaying products by category
@app.route('/product_by_category/<category>', methods=['GET'])
def product_by_category(category):
    all_products = get_all_products()
    return render_template('product_info.html', all_products=all_products, selected_category=category)

# @app.route('/add_to_cart/<product_id>', methods=['POST'])
# def add_to_cart(product_id):
#     # Retrieve product based on product_id (replace this with your actual product retrieval logic)
#     product = get_product_by_id(product_id)

#     if product:
#         shopping_cart.append(product)
#         flash(f'{product.name} added to cart!', 'success')
#     else:
#         flash(f'Product not found!', 'danger')

#     return redirect(url_for('product'))

if __name__ == '__main__':
    app.run(debug=True)
