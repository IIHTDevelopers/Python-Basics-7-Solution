    # Event Management System

from datetime import datetime

events = [
    ("Tech Conference", "2025-03-15", "2025-03-17", "New York"),
    ("Music Festival", "2025-04-20", "2025-04-22", "Los Angeles"),
    ("Art Exhibition", "2025-05-10", "2025-05-15", "Paris"),
    ("Startup Meetup", "2025-06-05", "2025-06-06", "London"),
    ("AI Summit", "2025-07-18", "2025-07-20", "Tokyo")
]

def display_upcoming_events():
        print("\nUpcoming Events:")
        for event in events:
            print(f"- {event[0]} from {event[1]} to {event[2]} at {event[3]}")

def count_total_events():
        print("\nTotal number of events:", len(events))

def longest_event_duration():
        max_duration_event = max(events, key=lambda e: (datetime.strptime(e[2], "%Y-%m-%d") - datetime.strptime(e[1], "%Y-%m-%d")).days)
        duration = (datetime.strptime(max_duration_event[2], "%Y-%m-%d") - datetime.strptime(max_duration_event[1], "%Y-%m-%d")).days
        print(f"\nEvent with the longest duration: {max_duration_event[0]} ({duration} days)")

if __name__ == "__main__":
        display_upcoming_events()
        count_total_events()
        longest_event_duration()