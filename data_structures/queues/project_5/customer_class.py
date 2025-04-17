from queue import Queue

class Customer:
    """
    A class representing a customer in the bank simulation.
    Attributes:
        id (str): Unique identifier for the customer.
        arrival_time (int): The time at which the customer arrives.
        wait (int): The time the customer has waited in the queue.
        service_time (int): The time taken to serve the customer.
    Methods:
        __init__(self, id, arrival_time): Initializes a new customer with an ID and arrival time.
        __str__(self): Returns a string representation of the customer.
    """
    def __init__(self, id, arrival_time):
        self.id = id 
        self.arrival_time = arrival_time
        self.wait = 0
        self.service_time = 0

    # Return a string representation of the customer class.
    def __str__(self):
        return f"({self.id}, {self.arrival_time}, {self.wait} minutes, {self.service_time} minutes)"


