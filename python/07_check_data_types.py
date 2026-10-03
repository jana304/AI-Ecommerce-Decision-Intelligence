import pandas as pd

orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")

print("\nORDERS DATA TYPES")
print(orders.dtypes)

print("\nORDER ITEMS DATA TYPES")
print(order_items.dtypes)

print("\nPAYMENTS DATA TYPES")
print(payments.dtypes)

print("\nREVIEWS DATA TYPES")
print(reviews.dtypes)

print("\nPRODUCTS DATA TYPES")
print(products.dtypes)