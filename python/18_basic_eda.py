import pandas as pd

# Load cleaned datasets
customers = pd.read_csv("data/cleaned/cleaned_customers.csv")
orders = pd.read_csv("data/cleaned/cleaned_orders.csv")
order_items = pd.read_csv("data/cleaned/cleaned_order_items.csv")
payments = pd.read_csv("data/cleaned/cleaned_payments.csv")

# Convert order date
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

print("===== BASIC E-COMMERCE ANALYSIS =====")

# 1. Total orders
print("\n1. Total Orders:", orders["order_id"].nunique())

# 2. Total customers
print("2. Total Customers:", customers["customer_unique_id"].nunique())

# 3. Total sales
total_sales = order_items["total_item_value"].sum()
print("3. Total Sales:", round(total_sales, 2))

# 4. Average order value
average_order_value = (
    order_items.groupby("order_id")["total_item_value"]
    .sum()
    .mean()
)

print("4. Average Order Value:", round(average_order_value, 2))

# 5. Order status
print("\n5. ORDER STATUS")
print(orders["order_status"].value_counts())

# 6. Monthly sales
order_items_with_date = order_items.merge(
    orders[["order_id", "order_purchase_timestamp"]],
    on="order_id",
    how="left"
)

order_items_with_date["month"] = (
    order_items_with_date["order_purchase_timestamp"]
    .dt.to_period("M")
)

monthly_sales = (
    order_items_with_date
    .groupby("month")["total_item_value"]
    .sum()
)

print("\n6. MONTHLY SALES")
print(monthly_sales)

# 7. Top customer states by number of customers
customer_states = (
    customers.groupby("customer_state")["customer_unique_id"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n7. TOP CUSTOMER STATES")
print(customer_states.head(10))

print("\n===== EDA COMPLETE =====")