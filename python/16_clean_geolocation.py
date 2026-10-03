import pandas as pd

# Load raw geolocation data
geo = pd.read_csv(
    "data/raw/olist_geolocation_dataset.csv"
)

print("Raw geolocation rows:", len(geo))

# Group by ZIP code prefix
geo_cleaned = (
    geo.groupby("geolocation_zip_code_prefix", as_index=False)
    .agg({
        "geolocation_lat": "mean",
        "geolocation_lng": "mean",
        "geolocation_city": "first",
        "geolocation_state": "first"
    })
)

# Standardize text fields
geo_cleaned["geolocation_city"] = (
    geo_cleaned["geolocation_city"]
    .str.strip()
    .str.lower()
)

geo_cleaned["geolocation_state"] = (
    geo_cleaned["geolocation_state"]
    .str.strip()
    .str.upper()
)

print("\nGeolocation cleaned successfully!")
print("Rows:", len(geo_cleaned))
print("Columns:", len(geo_cleaned.columns))

print("\nMissing values:")
print(geo_cleaned.isnull().sum())

print("\nFirst 5 rows:")
print(geo_cleaned.head())

# Save cleaned file
geo_cleaned.to_csv(
    "data/cleaned/cleaned_geolocation.csv",
    index=False
)

print("\nCleaned geolocation file saved successfully!")