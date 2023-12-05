from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, value):
        # Abstract method to be implemented by concrete observers.
        pass

# ConcreteObserver class
class ConcreteObserver(Observer):
    def update(self, value):
        # Implementation of the update method for ConcreteObserver.
        print(f"Counter value updated: {value}")

# Subject class
class VisitCounter:
    def __init__(self):
        # Initialize the counter and the list to store observers.
        self.counter = 0
        self.observers = []

    def attach(self, observer):
        # Add an observer to the list.
        self.observers.append(observer)

    def detach(self, observer):
        # Remove an observer from the list if it exists.
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        # Notify all observers with the current counter value.
        for observer in self.observers:
            observer.update(self.counter)

    def increment_counter(self):
        # Increment the counter and notify observers when it's a multiple of 3.
        self.counter += 1
        if self.counter % 3 == 0:
            self.notify_observers()
