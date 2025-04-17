import random
import os
from queues.project_5.queue_class import Queue
from queues.project_5.customer_class import Customer
from queues.project_5.simulator import BankSimulation
import sys

# Add the parent directory to the system path to allow imports from the project structure
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

def run(self):
    """
    Simulates the bank operation for a given duration.

    This function handles:
    - Random customer arrivals with a 50% chance per minute.
    - Serving customers in the queue if the teller is idle.
    - Tracking customer wait times and service times.
    - Moving customers to the served list once their service is complete.

    Args:
        self: The instance of the BankSimulation class.
    """
    for current_minute in range(1, self.duration + 1):
        # Random customer arrival
        if random.randint(0, 1) == 1:  # 50% chance
            customer = Customer(f"C{self.customer_id_counter}", current_minute)
            self.customer_id_counter += 1
            self.queue.enqueue(customer)

        # Check if a customer is being served
        if self.current_customer:
            if current_minute == self.service_end_time:
                # Add the served customer to the list and reset the teller
                self.customers_served.append(self.current_customer)
                self.current_customer = None

        # Serve the next customer if teller is idle
        if not self.current_customer and not self.queue.is_empty():
            self.current_customer = self.queue.dequeue()
            self.current_customer.wait_time = current_minute - self.current_customer.arrival_time
            self.current_customer.service_time = random.randint(1, 10)
            self.service_end_time = current_minute + self.current_customer.service_time

if __name__ == "__main__":
    """
    Entry point for the bank simulation.

    This block initializes the queue and simulation, runs the simulation,
    and prints a summary of the results, including:
    - Details of served customers.
    - Total and average wait and service times.
    - Customers still in the queue at the end of the simulation.
    """
    from queues.project_5.queue_class import Queue
    from queues.project_5.simulator import BankSimulation

    # Initialize the queue and simulation
    queue = Queue()
    simulation = BankSimulation(queue)
    simulation.run()

    # Print the results of the simulation
    print("\n=== Simulation Summary ===")
    for customer in simulation.customers_served:
        print(customer)

    if simulation.customers_served:
        # Calculate and display summary statistics
        total_wait = sum(c.wait_time for c in simulation.customers_served)
        total_service = sum(c.service_time for c in simulation.customers_served)
        count = len(simulation.customers_served)

        print(f"\nTotal customers served: {count}")
        print(f"Total waiting time: {total_wait} minutes")
        print(f"Total service time: {total_service} minutes")
        print(f"Average waiting time: {total_wait / count:.2f} minutes")
        print(f"Average service time: {total_service / count:.2f} minutes")

    # Display customers still in the queue
    print(f"\nCustomers still in queue: {simulation.queue.size()}")
    for customer in simulation.queue.items:
        wait_time = simulation.duration - customer.arrival_time
        print(f"{customer.id} is still waiting (waited {wait_time} minutes)")