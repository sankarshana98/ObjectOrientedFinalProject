from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        # Abstract method to be implemented by concrete observers.
        raise NotImplementedError

class NotificationObserver(Observer):
    def update(self, message):
        # Implementation of the update method for NotificationObserver.
        print(f"Notification: {message}")

class Subject:
    def __init__(self):
        # Initialize the list to store observers
        self.observers = []

    def attach(self, observer):
        # Add an observer to the list
        self.observers.append(observer)

    def detach(self, observer):
        # Remove an observer from the list
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, message):
        # Notify all observers with the given message
        for observer in self.observers:
            observer.update(message)