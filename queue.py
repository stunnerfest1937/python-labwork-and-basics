import random

customers = [10]

for i in range(10):
    arrival_time = float(input(f"Enter arrival time for customer {i + 1}: "))
    service_time = random.randint(2, 10)
    customers.append((arrival_time, service_time))
    print(f"Customer {i + 1} arrives at {arrival_time} and requires {service_time} minutes of service")

for arrival_time, service_time in customers:
    print(f"Customer can start receiving service after {arrival_time} minutes")



