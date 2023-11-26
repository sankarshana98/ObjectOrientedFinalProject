from observer import Observer
class User(Observer):
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} received a notification: {message}")