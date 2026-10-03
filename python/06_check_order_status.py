import pandas as pd

orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

print("Order Status Counts:")
print(orders["order_status"].value_counts())