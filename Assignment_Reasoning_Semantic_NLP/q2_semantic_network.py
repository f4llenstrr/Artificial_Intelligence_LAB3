semantic_network = [
    ("Airline", "operates", "Flight"),
    ("Flight", "has", "Departure Time"),
    ("Flight", "has", "Destination"),
    ("Passenger", "books", "Flight"),
    ("Flight", "can be", "Delayed"),
    ("Flight", "can be", "Cancelled"),
    ("Delay", "may cause", "Passenger Complaint")
]

for relationship in semantic_network:
    print(relationship)