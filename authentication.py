# authentication.py
from user import User

class AuthSingleton:
    _instance = None
    user_data = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(AuthSingleton, cls).__new__(cls)
            cls._instance.logged_in_user = None
        return cls._instance

    def create_user(self, username, password):
        # Simulating user data storage
        new_user = {"username": username, "password": password}
        self.user_data.append(new_user)
        print(f"User account created successfully")

    def login(self, username, password):
        # Simulating user authentication logic
        for user in self.user_data:
            if user["username"] == username and user["password"] == password:
                self.logged_in_user = User(username, password)
                print(f"User {username} logged in successfully.")
                return True
        print("Invalid username or password.")
        return False

    def logout(self):
        self.logged_in_user = None
        print("User logged out.")

    def get_logged_in_user(self):
        return self.logged_in_user

