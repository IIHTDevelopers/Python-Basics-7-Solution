import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Function 1: Get the Price of the Room with a Jacuzzi
def jacuzzi_room_price():
    rooms = get_room_data()
    for room_id, details in rooms.items():
        if "Jacuzzi" in details["amenities"]:
            return room_id, details["price"]
    return None, None

# Function 2: Calculate Total Revenue
# Function 3: Find the Most Expensive Room
def most_expensive_room():
    rooms = get_room_data()
    most_expensive = max(rooms.items(), key=lambda x: x[1]["price"])
    return most_expensive[0], most_expensive[1]["price"]

# Helper Functions
def get_room_data():
    return {
        "R101": {"type": "Standard", "price": 100.00, "capacity": 2, "amenities": ["TV", "WiFi"]},
        "R102": {"type": "Deluxe", "price": 150.00, "capacity": 2, "amenities": ["TV", "WiFi", "Mini Bar"]},
        "R103": {"type": "Suite", "price": 250.00, "capacity": 4, "amenities": ["TV", "WiFi", "Mini Bar", "Jacuzzi"]},
        "R104": {"type": "Standard", "price": 100.00, "capacity": 2, "amenities": ["TV", "WiFi"]},
        "R105": {"type": "Deluxe", "price": 150.00, "capacity": 2, "amenities": ["TV", "WiFi", "Mini Bar"]}
    }

def get_booking_data():
    today = datetime.now()
    return [
        {"booking_id": "B001", "room_id": "R102", "guest_name": "John Smith", "check_in": today - timedelta(days=2), "check_out": today + timedelta(days=3), "guests": 2},
        {"booking_id": "B002", "room_id": "R105", "guest_name": "Alice Johnson", "check_in": today + timedelta(days=5), "check_out": today + timedelta(days=10), "guests": 2},
        {"booking_id": "B003", "room_id": "R103", "guest_name": "Bob Williams", "check_in": today + timedelta(days=15), "check_out": today + timedelta(days=20), "guests": 3},
        {"booking_id": "B004", "room_id": "R101", "guest_name": "Emma Davis", "check_in": today + timedelta(days=7), "check_out": today + timedelta(days=9), "guests": 1},
        {"booking_id": "B005", "room_id": "R104", "guest_name": "Michael Brown", "check_in": today + timedelta(days=12), "check_out": today + timedelta(days=14), "guests": 2}
    ]

# Main Execution
def main():
    room_id, jacuzzi_price = jacuzzi_room_price()
    if room_id:
        print(f"Room with Jacuzzi: {room_id} (${jacuzzi_price:.2f})")
    else:
        print("No room with a Jacuzzi found.")

    room_id, price = most_expensive_room()
    print(f"Most Expensive Room: {room_id} (${price:.2f})")

if __name__ == "__main__":
    main()
