from abc import ABC, abstractmethod
from user import User
from authentication import AuthSingleton
import json 
from get_userId import get_user_id_by_username

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class LoginCommand(Command):
    def __init__(self, auth_instance, username, password):
        self.auth_instance = auth_instance
        self.username = username
        self.password = password

    def get_user_details(self, username):
        with open('users.json', 'r') as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username:
                return user

    def execute(self):
        # Get the user_id using the username
        user_id = get_user_id_by_username(self.username)

        # Perform the login operation
        return self.auth_instance.login(self.username, self.password, user_id)
    
# Concrete Command
class LogoutCommand(Command):
    def __init__(self, auth_instance):
        self.auth_instance = auth_instance

    def execute(self):
        self.auth_instance.logout()

# Invoker
class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command:
            self.command.execute()
