import pandas as pd

# ✅ Dataset
hotel_data = pd.DataFrame({
    "Hotel ID": [1, 2, 3, 4, 5],
    "Hotel Name": ["Grand Stay", "Comfort Inn", "Luxury Palace", "Budget Lodge", "Ocean View"],
    "Rating": [4.5, 3.8, 4.9, 3.2, 4.3],
    "Price Per Night": [2500, 1800, 4000, 1200, 3200]
})

# ✅ Function 1 - Filter hotels by minimum rating
def filter_hotels_by_rating(df, min_rating):
    """
    Filters and returns hotels with rating greater than or equal to min_rating.
    """
    return df[df["Rating"] >= min_rating]

# ✅ Function 2 - Calculate average price per night
def get_average_price(df):
    """
    Returns average price per night from the dataset.
    """
    return round(df["Price Per Night"].mean(), 2)

# ✅ Sample run block
if __name__ == "__main__":
    print("Hotels with Rating >= 4.0:\n", filter_hotels_by_rating(hotel_data, 4.0))
    print("Average Price Per Night:", get_average_price(hotel_data))
