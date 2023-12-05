from notification_observer import Subject

class VisitCounter(Subject):
    def __init__(self):
        # Initialize the VisitCounter as a subject (observable)
        super().__init__()

        # Initialize the counter to zero
        self.counter = 0

    def increment_counter(self):
        # Increment the counter
        self.counter += 1

        # Check if the counter is a multiple of 3
        if self.counter % 3 == 0:
            # Notify observers with a message about the user's visits
            self.notify_observers(f"User visited product details page {self.counter} times")
