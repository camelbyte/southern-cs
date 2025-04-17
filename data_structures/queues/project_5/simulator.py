import random
from queues.project_5.customer_class import Customer


class BankSimulation:
    """
    A class representing a bank simulation with a queue of customers.
    Attributes:
        queue (Queue): The queue of customers.
        duration (int): The duration of the simulation in minutes.
        current_customer (Customer): The customer currently being served.
        service_end_time (int): The time at which the current customer's service ends.
        customers_served (list): A list of customers who have been served.
        customer_id_counter (int): A counter for generating unique customer IDs.
    Methods:
        __init__(self, queue, duration=30): Initializes the simulation with a queue and duration.
        run(self): Runs the simulation for the specified duration.
    """
    def __init__(self, queue, duration=30):
        self.duration = duration
        self.queue = queue
        self.current_customer = None
        self.service_end_time = 0
        self.customers_served = []
        self.customer_id_counter = 1

    def run(self):
        for current_minute in range(1, self.duration + 1):
            print(f"\nMinute {current_minute} ")

            #  Randomizing code for arrivals
            if random.randint(0, 1) == 1:
                customer = Customer(f"C{self.customer_id_counter}", current_minute)
                self.customer_id_counter += 1
                self.queue.enqueue(customer)
                print(f"[+] Customer {customer.id} arrived at minute {current_minute}.")

            #  Check if current customer is finished
            if self.current_customer:
                if current_minute == self.service_end_time:
                    print(f"[✓] Finished serving {self.current_customer.id}.")
                    self.customers_served.append(self.current_customer)
                    self.current_customer = None
                else:
                    remaining = self.service_end_time - current_minute
                    print(f"[⏳] Serving {self.current_customer.id}, {remaining} min(s) left.")

            # Serve next customer
            if not self.current_customer and not self.queue.is_empty():
                self.current_customer = self.queue.dequeue()
                self.current_customer.wait_time = current_minute - self.current_customer.arrival_time
                self.current_customer.service_time = random.randint(1, 10)
                self.service_end_time = current_minute + self.current_customer.service_time
                print(f"Started serving {self.current_customer.id}. "
                      f"Waited: {self.current_customer.wait_time} min, "
                      f"Service: {self.current_customer.service_time} min.")
            elif not self.current_customer:
                print("Teller is idle. No customers to serve.")
