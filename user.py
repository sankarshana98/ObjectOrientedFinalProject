from observer import Observer
class User(Observer):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def __str__(self):
        return f"User: {self.username}"
    
    def update(self, message):
        print(f"{self.name} received a notification: {message}")