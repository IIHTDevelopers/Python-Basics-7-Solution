import pandas as pd

# ✅ Sample Dataset
membership_data = pd.DataFrame({
    "Member ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Membership Type": ["Gold", "Silver", "Gold", "Bronze", "Silver"],
    "Monthly Fee": [1500, 1000, 1500, 800, 1000],
    "Months Active": [12, 8, 6, 3, 10]
})

# ✅ Function 1: Arithmetic Logic - Total revenue per member
def calculate_total_contribution(df, member_id):
    """
    Return the total contribution made by a member using Monthly Fee × Months Active.
    """
    member = df[df["Member ID"] == member_id]
    if not member.empty:
        return int(member["Monthly Fee"].values[0] * member["Months Active"].values[0])
    return 0

# ✅ Function 2: Loop - Count members per membership type
def count_members_per_type(df):
    """
    Returns a dictionary with count of members in each membership type using a loop.
    """
    counts = {}
    for mtype in df["Membership Type"]:
        if mtype in counts:
            counts[mtype] += 1
        else:
            counts[mtype] = 1
    return counts

def is_alice_long_term(df):
    """
    Returns True if Alice has been active for more than 12 months.
    """
    alice = df[df["Name"].str.lower() == "alice"]
    if not alice.empty:
        return alice["Months Active"].values[0] > 12
    return False

# ✅ Sample Execution
if __name__ == "__main__":
    print("Total Contribution by Member 101:", calculate_total_contribution(membership_data, 101))
    print("Count of Members Per Type:", count_members_per_type(membership_data))
    print("Is Alice a long-term member (>12 months)?", is_alice_long_term(membership_data))
