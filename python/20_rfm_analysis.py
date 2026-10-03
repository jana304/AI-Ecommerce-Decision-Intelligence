import pandas as pd

# ==========================================
# 1. LOAD CUSTOMER SUMMARY
# ==========================================

customers = pd.read_csv(
    "data/cleaned/customer_summary.csv"
)

# Convert purchase dates
customers["first_purchase"] = pd.to_datetime(
    customers["first_purchase"]
)

customers["last_purchase"] = pd.to_datetime(
    customers["last_purchase"]
)


# ==========================================
# 2. SET REFERENCE DATE
# ==========================================

reference_date = customers["last_purchase"].max()


# ==========================================
# 3. CALCULATE RFM METRICS
# ==========================================

# Recency = days since customer's last purchase
customers["recency"] = (
    reference_date - customers["last_purchase"]
).dt.days

# Frequency = number of orders
customers["frequency"] = customers["total_orders"]

# Monetary = total customer spending
customers["monetary"] = customers["total_spend"]


# ==========================================
# 4. CREATE RFM SCORES
# ==========================================

# Recency:
# Lower number of days = better customer
customers["R_score"] = pd.qcut(
    customers["recency"],
    5,
    labels=[5, 4, 3, 2, 1],
    duplicates="drop"
)

# Frequency:
# Higher number of orders = better customer
customers["F_score"] = pd.qcut(
    customers["frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5],
    duplicates="drop"
)

# Monetary:
# Higher spending = better customer
customers["M_score"] = pd.qcut(
    customers["monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5],
    duplicates="drop"
)


# Convert scores to integers
customers["R_score"] = customers["R_score"].astype(int)
customers["F_score"] = customers["F_score"].astype(int)
customers["M_score"] = customers["M_score"].astype(int)


# ==========================================
# 5. COMBINED RFM SCORE
# ==========================================

customers["RFM_score"] = (
    customers["R_score"].astype(str)
    + customers["F_score"].astype(str)
    + customers["M_score"].astype(str)
)


# ==========================================
# 6. CUSTOMER SEGMENTATION
# ==========================================

def segment_customer(row):

    if (
        row["R_score"] >= 4
        and row["F_score"] >= 4
        and row["M_score"] >= 4
    ):
        return "Champions"

    elif (
        row["R_score"] >= 3
        and row["F_score"] >= 4
    ):
        return "Loyal Customers"

    elif (
        row["R_score"] >= 4
        and row["F_score"] <= 2
    ):
        return "New Customers"

    elif (
        row["R_score"] <= 2
        and row["F_score"] >= 3
    ):
        return "At Risk"

    elif (
        row["R_score"] <= 2
        and row["F_score"] <= 2
    ):
        return "Lost Customers"

    else:
        return "Potential Loyalists"


customers["customer_segment"] = customers.apply(
    segment_customer,
    axis=1
)


# ==========================================
# 7. DISPLAY RESULTS
# ==========================================

print("===== RFM ANALYSIS =====")

print("\nReference Date:")
print(reference_date)

print("\nRFM Summary:")

print(
    customers[
        [
            "recency",
            "frequency",
            "monetary"
        ]
    ].describe()
)


# ==========================================
# 8. CUSTOMER SEGMENTS
# ==========================================

print("\nCustomer Segments:")

print(
    customers["customer_segment"]
    .value_counts()
)


# ==========================================
# 9. AVERAGE SPENDING BY SEGMENT
# ==========================================

print("\nAverage Monetary Value by Segment:")

print(
    customers
    .groupby("customer_segment")["monetary"]
    .mean()
    .sort_values(ascending=False)
)


# ==========================================
# 10. TOP 10 RFM CUSTOMERS
# ==========================================

print("\nTop 10 RFM Customers:")

top_customers = (
    customers
    .sort_values(
        ["R_score", "F_score", "M_score"],
        ascending=False
    )
    .head(10)
)

print(
    top_customers[
        [
            "customer_unique_id",
            "recency",
            "frequency",
            "monetary",
            "R_score",
            "F_score",
            "M_score",
            "RFM_score",
            "customer_segment"
        ]
    ]
)


# ==========================================
# 11. SAVE RFM DATASET
# ==========================================

customers.to_csv(
    "data/cleaned/rfm_customer_segments.csv",
    index=False
)

print("\nRFM analysis completed!")
print("RFM dataset saved successfully!")