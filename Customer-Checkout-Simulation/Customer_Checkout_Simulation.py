from collections import deque

def checkout_simulation(customers, service_time):
    # Initialize the queue with customer names
    queue = deque(customers)

    # Variable to track the total wait time
    total_wait_time = 0
    current_time = 0  # Tracks the time as customers are served

    # Process each customer in the queue
    while queue:
        customer = queue.popleft()  # Dequeue the next customer
        print(f"Serving customer: {customer}")
        
        # Wait time for the current customer
        wait_time_for_customer = current_time
        total_wait_time += wait_time_for_customer
        
        # Update current time by adding the service time for the current customer
        current_time += service_time
    
    # After all customers have been served, print the total wait time
    print(f"\nTotal wait time: {total_wait_time} minutes")

# Input data
customers = ["Alice", "Bob", "Charlie", "Diana"]
service_time = 5  # Fixed service time per customer

# Run the simulation
checkout_simulation(customers, service_time)

