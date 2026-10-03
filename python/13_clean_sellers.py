import pandas as pd

# Load raw sellers
sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")

# Standardize text fields
sellers["seller_city"] = sellers["seller_city"].str.strip().str.lower()
sellers["seller_state"] = sellers["seller_state"].str.strip().str.upper()

print("Sellers cleaned successfully!")
print("Rows:", len(sellers))
print("Columns:", len(sellers.columns))

print("\nMissing values:")
print(sellers.isnull().sum())

print("\nFirst 5 rows:")
print(sellers.head())

# Save cleaned file
sellers.to_csv(
    "data/cleaned/cleaned_sellers.csv",
    index=False
)

print("\nCleaned sellers file saved successfully!")