import pandas as pd

# Load cleaned datasets
customers = pd.read_csv("data/cleaned/cleaned_customers.csv")
orders = pd.read_csv("data/cleaned/cleaned_orders.csv")
order_items = pd.read_csv("data/cleaned/cleaned_order_items.csv")

# Convert order date
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

# Keep useful order information
customer_orders = orders[
    [
        "order_id",
        "customer_id",
        "order_purchase_timestamp",
        "order_status"
    ]
].merge(
    customers[
        [
            "customer_id",
            "customer_unique_id",
            "customer_state"
        ]
    ],
    on="customer_id",
    how="left"
)

# Calculate order value
order_values = (
    order_items
    .groupby("order_id")["total_item_value"]
    .sum()
    .reset_index()
)

customer_orders = customer_orders.merge(
    order_values,
    on="order_id",
    how="left"
)

# Customer-level analysis
customer_summary = (
    customer_orders
    .groupby("customer_unique_id")
    .agg(
        total_orders=("order_id", "nunique"),
        total_spend=("total_item_value", "sum"),
        first_purchase=("order_purchase_timestamp", "min"),
        last_purchase=("order_purchase_timestamp", "max"),
        customer_state=("customer_state", "first")
    )
    .reset_index()
)

# Customer type
customer_summary["customer_type"] = customer_summary[
    "total_orders"
].apply(
    lambda x: "Repeat Customer" if x > 1 else "One-Time Customer"
)

# Summary
total_customers = len(customer_summary)

repeat_customers = (
    customer_summary["total_orders"] > 1
).sum()

one_time_customers = (
    customer_summary["total_orders"] == 1
).sum()

repeat_purchase_rate = (
    repeat_customers / total_customers
) * 100

average_customer_spend = (
    customer_summary["total_spend"].mean()
)

print("===== CUSTOMER ANALYSIS =====")

print("\nTotal Customers:", total_customers)
print("Repeat Customers:", repeat_customers)
print("One-Time Customers:", one_time_customers)

print(
    "Repeat Purchase Rate:",
    round(repeat_purchase_rate, 2),
    "%"
)

print(
    "Average Customer Spend:",
    round(average_customer_spend, 2)
)

print("\nCustomer Type:")
print(
    customer_summary["customer_type"]
    .value_counts()
)

print("\nTop 10 Customers by Spend:")
print(
    customer_summary
    .sort_values("total_spend", ascending=False)
    .head(10)
)

# Save customer-level dataset
customer_summary.to_csv(
    "data/cleaned/customer_summary.csv",
    index=False
)

print("\nCustomer analysis completed!")
print("Customer summary saved successfully!")