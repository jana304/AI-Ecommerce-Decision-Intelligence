import pandas as pd

# Load raw products
products = pd.read_csv("data/raw/olist_products_dataset.csv")

print("Original missing values:")
print(products.isnull().sum())

# Fill missing category
products["product_category_name"] = products["product_category_name"].fillna("unknown")

# Fill missing numeric values with 0
numeric_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for column in numeric_columns:
    products[column] = products[column].fillna(0)

print("\nMissing values after cleaning:")
print(products.isnull().sum())

print("\nProducts cleaned successfully!")
print("Rows:", len(products))
print("Columns:", len(products.columns))

# Save cleaned file
products.to_csv(
    "data/cleaned/cleaned_products.csv",
    index=False
)

print("\nCleaned products file saved successfully!")