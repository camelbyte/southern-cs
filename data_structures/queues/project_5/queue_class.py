from queues.project_5.customer_class import Customer

class Queue:
    """
    A class representing a queue of customers.
    Attributes:
        items (list): A list to hold the customers in the queue.
    Methods:
        __init__(self): Initializes an empty queue.
        enqueue(customer): Adds a customer to the end of the queue.
        dequeue(): Removes and returns the customer at the front of the queue.
        peek(): Returns the customer at the front of the queue without removing them.
        is_empty(): Checks if the queue is empty.
        size(): Returns the number of customers in the queue.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, customer):
        self.items.append(customer)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

