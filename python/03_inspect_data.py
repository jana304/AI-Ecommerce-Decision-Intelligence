import pandas as pd

customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")
geolocation = pd.read_csv("data/raw/olist_geolocation_dataset.csv")
category_translation = pd.read_csv(
    "data/raw/product_category_name_translation.csv"
)

print("\nCUSTOMERS")
print(customers.columns.tolist())

print("\nORDERS")
print(orders.columns.tolist())

print("\nORDER ITEMS")
print(order_items.columns.tolist())

print("\nPAYMENTS")
print(payments.columns.tolist())

print("\nREVIEWS")
print(reviews.columns.tolist())

print("\nPRODUCTS")
print(products.columns.tolist())

print("\nSELLERS")
print(sellers.columns.tolist())

print("\nGEOLOCATION")
print(geolocation.columns.tolist())

print("\nCATEGORY TRANSLATION")
print(category_translation.columns.tolist())