# Import necessary modules
from abc import ABC, abstractmethod
from user import User
from authentication import AuthSingleton
import json
from get_userId import get_user_id_by_username

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        """
        Abstract method to be implemented by concrete command classes.
        It defines the common interface for all concrete command classes.
        """
        pass

# Concrete Command
class LoginCommand(Command):
    def __init__(self, auth_instance, username, password):
        """
        Concrete command class for handling user login.

        Parameters:
        - auth_instance (AuthSingleton): An instance of the authentication system.
        - username (str): The username entered by the user.
        - password (str): The password entered by the user.
        """
        self.auth_instance = auth_instance
        self.username = username
        self.password = password

    def get_user_details(self, username):
        """
        Retrieve user details (e.g., full name, email) based on the username from a JSON file.

        Parameters:
        - username (str): The username for which user details are to be retrieved.

        Returns:
        - dict: User details as a dictionary.
        """
        with open('users.json', 'r') as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username:
                return user

    def execute(self):
        """
        Implementation of the execute method for the LoginCommand.
        Retrieves the user_id using the provided username and performs the login operation.
        """
        # Get the user_id using the username
        user_id = get_user_id_by_username(self.username)

        # Perform the login operation
        return self.auth_instance.login(self.username, self.password, user_id)

# Concrete Command
class LogoutCommand(Command):
    def __init__(self, auth_instance):
        """
        Concrete command class for handling user logout.

        Parameters:
        - auth_instance (AuthSingleton): An instance of the authentication system.
        """
        self.auth_instance = auth_instance

    def execute(self):
        """
        Implementation of the execute method for the LogoutCommand.
        Calls the logout method of the authentication instance.
        """
        self.auth_instance.logout()

# Invoker
class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        """
        Set the command to be executed by the invoker.

        Parameters:
        - command (Command): An instance of a concrete command class.
        """
        self.command = command

    def execute_command(self):
        """
        Execute the command previously set in the invoker.
        """
        if self.command:
            self.command.execute()
