import pandas as pd

# ==========================================
# 1. LOAD PROJECT DATA
# ==========================================

customers = pd.read_csv(
    "data/cleaned/cleaned_customers.csv"
)

orders = pd.read_csv(
    "data/cleaned/cleaned_orders.csv"
)

order_items = pd.read_csv(
    "data/cleaned/cleaned_order_items.csv"
)

rfm = pd.read_csv(
    "data/cleaned/rfm_customer_segments.csv"
)


# ==========================================
# 2. CALCULATE SALES METRICS
# ==========================================

total_orders = orders["order_id"].nunique()

total_customers = customers["customer_unique_id"].nunique()

total_sales = order_items["total_item_value"].sum()

order_sales = (
    order_items
    .groupby("order_id")["total_item_value"]
    .sum()
)

average_order_value = order_sales.mean()


# ==========================================
# 3. CUSTOMER RETENTION
# ==========================================

repeat_customers = (
    rfm["frequency"] > 1
).sum()

repeat_rate = (
    repeat_customers / total_customers
) * 100


# ==========================================
# 4. RFM ANALYSIS
# ==========================================

top_segment = (
    rfm.groupby("customer_segment")["monetary"]
    .mean()
    .sort_values(ascending=False)
    .index[0]
)

average_customer_spend = rfm["monetary"].mean()


# ==========================================
# 5. DELIVERY PERFORMANCE
# ==========================================

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"],
    errors="coerce"
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"],
    errors="coerce"
)

delivered_orders = orders[
    orders["order_delivered_customer_date"].notna()
].copy()

# Actual delivery time
delivered_orders["delivery_days"] = (
    delivered_orders["order_delivered_customer_date"]
    - delivered_orders["order_purchase_timestamp"]
).dt.total_seconds() / 86400

average_delivery_days = (
    delivered_orders["delivery_days"].mean()
)

# Delivery delay compared with estimated delivery date
delivered_orders["delivery_delay_days"] = (
    delivered_orders["order_delivered_customer_date"]
    - delivered_orders["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

# Late delivery = delivered after estimated date
late_delivery_rate = (
    delivered_orders["delivery_delay_days"] > 0
).mean() * 100


# ==========================================
# 6. GENERATE BUSINESS INSIGHTS
# ==========================================

insights = []

# Customer retention insight
if repeat_rate < 5:
    insights.append(
        f"Customer retention is an important opportunity because "
        f"the repeat customer rate is {repeat_rate:.2f}%."
    )

# Order value insight
if average_order_value > 150:
    insights.append(
        f"The average order value is {average_order_value:.2f}, "
        "indicating meaningful value per order."
    )

# Overall business performance
insights.append(
    f"The analysis contains {total_orders:,} orders and "
    f"{total_customers:,} customers with total sales value of "
    f"{total_sales:,.2f}."
)

# RFM insight
insights.append(
    f"{top_segment} has the highest average customer spending "
    f"among the RFM segments."
)

# Customer segmentation recommendation
insights.append(
    "RFM segmentation can support targeted campaigns for "
    "new, loyal, at-risk and lost customers."
)

# Late delivery insight
if late_delivery_rate > 5:
    insights.append(
        f"Delivery performance needs attention because "
        f"{late_delivery_rate:.2f}% of delivered orders were late."
    )

# Delivery time insight
if average_delivery_days > 10:
    insights.append(
        f"Average delivery time is {average_delivery_days:.2f} days, "
        "highlighting an opportunity to improve logistics efficiency."
    )


# ==========================================
# 7. DISPLAY RESULTS
# ==========================================

print("\n==========================================")
print("AI-ASSISTED BUSINESS INSIGHTS")
print("==========================================")

print(f"\nTotal Orders: {total_orders:,}")

print(
    f"Total Customers: {total_customers:,}"
)

print(
    f"Total Sales Value: {total_sales:,.2f}"
)

print(
    f"Average Order Value: {average_order_value:.2f}"
)

print(
    f"Repeat Customer Rate: {repeat_rate:.2f}%"
)

print(
    f"Top RFM Segment by Average Spend: {top_segment}"
)

print(
    f"Average Delivery Time: {average_delivery_days:.2f} days"
)

print(
    f"Late Delivery Rate: {late_delivery_rate:.2f}%"
)

print("\nBUSINESS INSIGHTS:\n")

for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")

print("\nAnalysis completed successfully.")
# ==========================================
# 8. SAVE INSIGHTS TO DOCUMENTATION
# ==========================================

with open(
    "documentation/ai_business_insights.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write("AI-ASSISTED BUSINESS INSIGHTS\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Orders: {total_orders:,}\n")
    file.write(f"Total Customers: {total_customers:,}\n")
    file.write(f"Total Sales Value: {total_sales:,.2f}\n")
    file.write(f"Average Order Value: {average_order_value:.2f}\n")
    file.write(f"Repeat Customer Rate: {repeat_rate:.2f}%\n")
    file.write(f"Top RFM Segment by Average Spend: {top_segment}\n")
    file.write(f"Average Delivery Time: {average_delivery_days:.2f} days\n")
    file.write(f"Late Delivery Rate: {late_delivery_rate:.2f}%\n\n")

    file.write("BUSINESS INSIGHTS\n")
    file.write("=" * 40 + "\n\n")

    for i, insight in enumerate(insights, 1):
        file.write(f"{i}. {insight}\n")

print("Insights saved to documentation/ai_business_insights.txt")