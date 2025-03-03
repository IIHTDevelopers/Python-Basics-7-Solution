import os


def create_membership_file():
    filename = "membership_data.txt"
    data = """John, Gold, 2024-01-15, 2025-01-15, Paid
Alice, Silver, 2024-02-01, 2025-02-01, Unpaid
Bob, Platinum, 2024-03-10, 2025-03-10, Paid
Emma, Gold, 2024-04-20, 2025-04-20, Paid
Mike, Silver, 2024-05-05, 2025-05-05, Unpaid"""

    with open(filename, "w") as file:
        file.write(data)

    print(f"Sample file '{filename}' created successfully.")


def check_membership_status():
    active_members = {}
    with open("membership_data.txt", "r") as file:
        for line in file:
            name, plan, start_date, end_date, status = line.strip().split(", ")
            if status == "Paid":
                active_members[name] = {"plan": plan, "end_date": end_date}
    print("\nActive Gym Members:")
    for member, details in active_members.items():
        print(f"- {member}: {details['plan']} Plan (Valid till {details['end_date']})")


def count_members_by_plan():
    plan_counts = {"Gold": 0, "Silver": 0, "Platinum": 0}
    
    with open("membership_data.txt", "r") as file:
        for line in file:
            name, plan, start_date, end_date, status = line.strip().split(", ")
            if plan in plan_counts:
                plan_counts[plan] += 1
    
    print("\nMembership Plan Distribution:")
    for plan, count in plan_counts.items():
        print(f"- {plan}: {count} members")
    
    return plan_counts


if __name__ == "__main__":
    create_membership_file()
    check_membership_status()
    count_members_by_plan()
