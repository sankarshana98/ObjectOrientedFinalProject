from user import User
import uuid
import os
import json

class AuthSingleton:
    _instance = None

    def __new__(cls):
        """
        Implement a singleton pattern for AuthSingleton.

        Returns:
        - AuthSingleton: An instance of the AuthSingleton class.
        """
        if not cls._instance:
            cls._instance = super(AuthSingleton, cls).__new__(cls)
            cls._instance.logged_in_user = None
            cls._instance.load_user_data()
        return cls._instance

    def create_user(self, username, password, full_name, email, profile_pic=None):
        """
        Create a new user and save the user data.

        Parameters:
        - username (str): The username for the new user.
        - password (str): The password for the new user.
        - full_name (str): The full name of the new user.
        - email (str): The email address of the new user.
        - profile_pic (File): The profile picture file for the new user (optional).
        """
        # Simulating user data storage
        user_id = str(uuid.uuid4())
        user_data = {
            "user_id": user_id,
            "username": username,
            "password": password,
            "full_name": full_name,
            "email": email,
            "profile_pic": None  # Default to None initially
        }

        # Save profile picture if provided
        if profile_pic:
            filename = self.save_profile_picture(profile_pic)
            user_data["profile_pic"] = filename

        # Append the new user data
        self.user_data.append(user_data)

        # Write the updated user data back to the JSON file
        self.save_user_data()

        print(f"User account created successfully")

    def load_user_data(self):
        """
        Load user data from the 'users.json' file.
        """
        try:
            with open('users.json', 'r') as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = []

    def save_user_data(self):
        """
        Save user data to the 'users.json' file.
        """
        with open('users.json', 'w') as file:
            json.dump(self.user_data, file, indent=2)

    def save_profile_picture(self, profile_pic):
        """
        Save a user's profile picture.

        Parameters:
        - profile_pic (File): The profile picture file to be saved.

        Returns:
        - str: The filename under which the profile picture is saved.
        """
        # Save the file with a unique name (you may want to add more logic for file handling)
        filename = str(uuid.uuid4()) + os.path.splitext(profile_pic.filename)[1]
        profile_pic.save(os.path.join("static/profile_pics", filename))
        return filename

    def login(self, username, password):
        """
        Simulate user login authentication.

        Parameters:
        - username (str): The username for login.
        - password (str): The password for login.

        Returns:
        - bool: True if login is successful, False otherwise.
        """
        user = self.get_user_by_username(username)
        if user and user["password"] == password:
            self.logged_in_user = user
            print(f"User {username} logged in successfully.")
            return True
        print("Invalid username or password.")
        return False

    def logout(self):
        """
        Log the user out by setting logged_in_user to None.
        """
        self.logged_in_user = None
        print("User logged out.")

    def get_logged_in_user(self):
        """
        Get the currently logged-in user.

        Returns:
        - dict or None: The user information if a user is logged in, None otherwise.
        """
        return self.logged_in_user

    def get_user_by_username(self, username):
        """
        Get user information by username.

        Parameters:
        - username (str): The username to search for.

        Returns:
        - dict or None: User information if found, None otherwise.
        """
        for user in self.user_data:
            if user["username"] == username:
                return user
        return None
