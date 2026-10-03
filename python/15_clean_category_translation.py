import pandas as pd

# Load raw category translation
categories = pd.read_csv(
    "data/raw/product_category_name_translation.csv"
)

# Standardize text fields
categories["product_category_name"] = (
    categories["product_category_name"]
    .str.strip()
    .str.lower()
)

categories["product_category_name_english"] = (
    categories["product_category_name_english"]
    .str.strip()
    .str.lower()
)

print("Category translation cleaned successfully!")
print("Rows:", len(categories))
print("Columns:", len(categories.columns))

print("\nMissing values:")
print(categories.isnull().sum())

print("\nFirst 10 rows:")
print(categories.head(10))

# Save cleaned file
categories.to_csv(
    "data/cleaned/cleaned_category_translation.csv",
    index=False
)

print("\nCleaned category translation file saved successfully!")