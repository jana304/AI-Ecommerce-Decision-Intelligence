import pandas as pd

# Load raw customers
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")

# Remove extra spaces and standardize text
customers["customer_city"] = customers["customer_city"].str.strip().str.lower()
customers["customer_state"] = customers["customer_state"].str.strip().str.upper()

print("Customers cleaned successfully!")
print("Rows:", len(customers))
print("Columns:", len(customers.columns))

print("\nMissing values:")
print(customers.isnull().sum())

print("\nFirst 5 rows:")
print(customers.head())

# Save cleaned file
customers.to_csv(
    "data/cleaned/cleaned_customers.csv",
    index=False
)

print("\nCleaned customers file saved successfully!")