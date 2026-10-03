import pandas as pd

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

orders = pd.read_csv(
    "data/cleaned/cleaned_orders.csv"
)

reviews = pd.read_csv(
    "data/cleaned/cleaned_reviews.csv"
)

order_items = pd.read_csv(
    "data/cleaned/cleaned_order_items.csv"
)

sellers = pd.read_csv(
    "data/cleaned/cleaned_sellers.csv"
)


# ==========================================
# 2. CONVERT DATE COLUMNS
# ==========================================

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"]
)


# ==========================================
# 3. DELIVERY ANALYSIS
# ==========================================

delivered_orders = orders[
    orders["order_delivered_customer_date"].notna()
].copy()

average_delivery_days = delivered_orders[
    "delivery_days"
].mean()

late_delivery_rate = (
    delivered_orders["delivery_delay_days"] > 0
).mean() * 100

early_delivery_rate = (
    delivered_orders["delivery_delay_days"] <= 0
).mean() * 100


# ==========================================
# 4. REVIEW ANALYSIS
# ==========================================

average_review_score = reviews["review_score"].mean()

review_distribution = (
    reviews["review_score"]
    .value_counts()
    .sort_index()
)


# ==========================================
# 5. SELLER ANALYSIS
# ==========================================

seller_orders = (
    order_items
    .groupby("seller_id")
    .agg(
        orders_handled=("order_id", "nunique"),
        units_sold=("order_item_id", "count"),
        sales_value=("total_item_value", "sum")
    )
    .reset_index()
    .sort_values(
        "sales_value",
        ascending=False
    )
)


# ==========================================
# 6. ORDER STATUS ANALYSIS
# ==========================================

order_status = (
    orders["order_status"]
    .value_counts()
    .reset_index()
)

order_status.columns = [
    "order_status",
    "order_count"
]


# ==========================================
# 7. DISPLAY RESULTS
# ==========================================

print("===== OPERATIONAL ANALYSIS =====")

print("\nDelivered Orders:")
print(len(delivered_orders))

print("\nAverage Delivery Time (Days):")
print(round(average_delivery_days, 2))

print("\nLate Delivery Rate:")
print(round(late_delivery_rate, 2), "%")

print("\nEarly / On-Time Delivery Rate:")
print(round(early_delivery_rate, 2), "%")

print("\nAverage Review Score:")
print(round(average_review_score, 2))

print("\nReview Score Distribution:")
print(review_distribution)

print("\nOrder Status Distribution:")
print(order_status)

print("\nTop 10 Sellers by Sales Value:")
print(
    seller_orders.head(10)
)


# ==========================================
# 8. SAVE RESULTS
# ==========================================

delivery_summary = pd.DataFrame({
    "metric": [
        "Delivered Orders",
        "Average Delivery Days",
        "Late Delivery Rate",
        "Early/On-Time Delivery Rate",
        "Average Review Score"
    ],
    "value": [
        len(delivered_orders),
        round(average_delivery_days, 2),
        round(late_delivery_rate, 2),
        round(early_delivery_rate, 2),
        round(average_review_score, 2)
    ]
})

delivery_summary.to_csv(
    "data/cleaned/delivery_summary.csv",
    index=False
)

seller_orders.to_csv(
    "data/cleaned/seller_performance.csv",
    index=False
)

order_status.to_csv(
    "data/cleaned/order_status_summary.csv",
    index=False
)


print("\nOperational analysis completed!")
print("Delivery summary saved successfully!")
print("Seller performance saved successfully!")
print("Order status summary saved successfully!")