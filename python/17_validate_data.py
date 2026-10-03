import pandas as pd

# Load cleaned datasets
customers = pd.read_csv("data/cleaned/cleaned_customers.csv")
orders = pd.read_csv("data/cleaned/cleaned_orders.csv")
order_items = pd.read_csv("data/cleaned/cleaned_order_items.csv")
payments = pd.read_csv("data/cleaned/cleaned_payments.csv")
products = pd.read_csv("data/cleaned/cleaned_products.csv")
reviews = pd.read_csv("data/cleaned/cleaned_reviews.csv")
sellers = pd.read_csv("data/cleaned/cleaned_sellers.csv")

print("===== DATA VALIDATION =====")

# Orders → Customers
missing = ~orders["customer_id"].isin(customers["customer_id"])
print("\nOrders → Customers")
print("Missing customer IDs:", missing.sum())

# Order Items → Orders
missing = ~order_items["order_id"].isin(orders["order_id"])
print("\nOrder Items → Orders")
print("Missing order IDs:", missing.sum())

# Payments → Orders
missing = ~payments["order_id"].isin(orders["order_id"])
print("\nPayments → Orders")
print("Missing order IDs:", missing.sum())

# Reviews → Orders
missing = ~reviews["order_id"].isin(orders["order_id"])
print("\nReviews → Orders")
print("Missing order IDs:", missing.sum())

# Order Items → Products
missing = ~order_items["product_id"].isin(products["product_id"])
print("\nOrder Items → Products")
print("Missing product IDs:", missing.sum())

# Order Items → Sellers
missing = ~order_items["seller_id"].isin(sellers["seller_id"])
print("\nOrder Items → Sellers")
print("Missing seller IDs:", missing.sum())

print("\n===== VALIDATION COMPLETE =====")