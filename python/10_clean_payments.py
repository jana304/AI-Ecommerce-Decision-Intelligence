import pandas as pd

# Load raw payments
payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")

# Check missing values
print("Payments cleaned successfully!")
print("Rows:", len(payments))
print("Columns:", len(payments.columns))

print("\nMissing values:")
print(payments.isnull().sum())

print("\nPayment types:")
print(payments["payment_type"].value_counts())

print("\nPayment value summary:")
print(payments["payment_value"].describe())

# Save cleaned file
payments.to_csv(
    "data/cleaned/cleaned_payments.csv",
    index=False
)

print("\nCleaned payments file saved successfully!")