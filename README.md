# Recommendations Engine Web Application

## Introduction

Welcome to the Recommendations Engine Web Application! This Flask-based web application provides a user interface for interacting with the recommendations engine. Users can create accounts, log in, view products, receive recommendations, and manage their profiles.

## Features

- **User Authentication**: Create accounts, log in, and log out securely.
- **Product Interaction**: View and interact with product information.
- **Recommendations**: Receive personalized product recommendations.
- **User Profile**: View and update user profile information.
- **Order History**: Track previous orders.
- **Notification**: Notify user for new recommendations.


## Getting Started

To get started with the Recommendations Engine Web Application, follow these steps:

1. **Clone the Repository**: `git clone https://github.com/sankarshana98/ObjectOrientedFinalProject.git`
2. **Install Dependencies**: `pip install Flask`
3. **Run the Application**: `python app.py`
4. **Access the Application**: Visit `http://localhost:5000/` in your web browser.

## Usage

The Recommendations Engine Web Application provides a user-friendly interface for users to interact with the recommendations engine. Users can perform the following actions:

- **Create User**: Register for a new account with a unique username and password.
- **Login**: Log in securely to access personalized features.
- **View Products**: Explore a variety of products with detailed information.
- **Product Details**: View detailed information about a specific product, including personalized recommendations.
- **Update Profile**: Modify user profile information such as full name and email.
- **Logout**: Log out securely to protect user accounts.

## Routes

- **Home**: `/` - Landing page with a welcome message for logged-in users.
- **Create User**: `/create_user` - Page for creating a new user account.
- **Login**: `/login` - Page for user login.
- **Product Information**: `/product_info` - Page displaying products, recommendations, and checkout functionality.
- **Logout**: `/logout` - Logout route to securely log out users.
- **Dashboard**: `/dashboard` - User dashboard with product information.
- **Product by Category**: `/product_by_category/<category>` - View products filtered by category.
- **View Profile**: `/view_profile` - View user profile details.
- **Update Profile**: `/update_profile` - Update user profile information.
- **Products**: `/products` - Display all available products.
- **Product Details**: `/product/<int:product_id>` - View details of a specific product, including recommendations.
- **Previous Orders**: `/previous_orders` - View the order history for the logged-in user.


<div align="center">

![UML](/images/chatuml_diagram.png)
<p><strong>UML Diagram.</strong></p>

![Create User](/images/1.png)
<p><strong>Create User.</strong></p>

<br>

![Welcome](/images/2.png)
<p><strong>Welcome.</strong></p>

<br>

![List of Products](/images/3.png)
<p><strong>List of Products.</strong></p>

<br>

![Product Details](/images/4.png)
<p><strong>Product Details page with recommendations.</strong></p>

<br>

![User Profile](/images/6.png)
<p><strong>User Profile.</strong></p>

</div>
