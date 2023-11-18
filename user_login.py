from abc import ABC, abstractmethod
from user import User
from authentication import AuthSingleton

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

    def execute(self):
        return self.auth_instance.login(self.username, self.password)

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
