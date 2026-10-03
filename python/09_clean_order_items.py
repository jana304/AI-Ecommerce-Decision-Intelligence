import pandas as pd

# Load raw order items
items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

# Convert shipping date to datetime
items["shipping_limit_date"] = pd.to_datetime(
    items["shipping_limit_date"],
    errors="coerce"
)

# Calculate total item value
items["total_item_value"] = (
    items["price"] + items["freight_value"]
)

print("Order items cleaned successfully!")
print("Rows:", len(items))
print("Columns:", len(items.columns))

print("\nMissing values:")
print(items.isnull().sum())

print("\nData types:")
print(items.dtypes)

# Save cleaned file
items.to_csv(
    "data/cleaned/cleaned_order_items.csv",
    index=False
)

print("\nCleaned order items file saved successfully!")