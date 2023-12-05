class Observer:
    def update(self, message):
        """
        Abstract method to be implemented by subclasses.
        This method is called by the subject to notify the observer about a change.

        Parameters:
        - message (str): The message or information being passed to the observer.
        """
        pass


class ProductSubject:
    def __init__(self):
        """
        Initialize a ProductSubject instance.

        Attributes:
        - observers (list): A list to store observer instances.
        """
        self.observers = []

    def add_observer(self, observer):
        """
        Add an observer to the list of observers.

        Parameters:
        - observer (Observer): An instance of the observer to be added.
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Remove an observer from the list of observers.

        Parameters:
        - observer (Observer): An instance of the observer to be removed.
        """
        self.observers.remove(observer)

    def notify_observers(self, message):
        """
        Notify all registered observers about a change.

        Parameters:
        - message (str): The message or information to be passed to the observers.
        """
        for observer in self.observers:
            observer.update(message)
