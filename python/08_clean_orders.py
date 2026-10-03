import pandas as pd

# Load raw orders data
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

# Date columns
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

# Convert dates
for column in date_columns:
    orders[column] = pd.to_datetime(orders[column], errors="coerce")

# Create delivery time in days
orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.days

# Create estimated delivery difference
orders["delivery_delay_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_estimated_delivery_date"]
).dt.days

# Save cleaned file
orders.to_csv("data/cleaned/cleaned_orders.csv", index=False)

print("Cleaned orders file created successfully!")
print("Rows:", len(orders))
print("Columns:", len(orders.columns))