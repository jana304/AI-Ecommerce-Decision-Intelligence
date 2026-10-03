import pandas as pd

# ==========================================
# 1. LOAD CLEANED DATA
# ==========================================

products = pd.read_csv(
    "data/cleaned/cleaned_products.csv"
)

order_items = pd.read_csv(
    "data/cleaned/cleaned_order_items.csv"
)

categories = pd.read_csv(
    "data/cleaned/cleaned_category_translation.csv"
)

reviews = pd.read_csv(
    "data/cleaned/cleaned_reviews.csv"
)


# ==========================================
# 2. ADD ENGLISH CATEGORY NAMES
# ==========================================

products = products.merge(
    categories,
    on="product_category_name",
    how="left"
)

# Replace missing English category names
products["product_category_name_english"] = (
    products["product_category_name_english"]
    .fillna("unknown")
)


# ==========================================
# 3. MERGE PRODUCTS WITH ORDER ITEMS
# ==========================================

product_sales = order_items.merge(
    products[
        [
            "product_id",
            "product_category_name_english"
        ]
    ],
    on="product_id",
    how="left"
)


# ==========================================
# 4. PRODUCT-LEVEL ANALYSIS
# ==========================================

product_summary = (
    product_sales
    .groupby("product_id")
    .agg(
        units_sold=("order_item_id", "count"),
        total_sales=("total_item_value", "sum"),
        average_item_value=("total_item_value", "mean"),
        category=("product_category_name_english", "first")
    )
    .reset_index()
)


# ==========================================
# 5. CATEGORY-LEVEL ANALYSIS
# ==========================================

category_summary = (
    product_sales
    .groupby("product_category_name_english")
    .agg(
        units_sold=("order_item_id", "count"),
        total_sales=("total_item_value", "sum"),
        average_item_value=("total_item_value", "mean"),
        unique_products=("product_id", "nunique")
    )
    .reset_index()
    .sort_values(
        "total_sales",
        ascending=False
    )
)


# ==========================================
# 6. PRODUCT RATING ANALYSIS
# ==========================================

review_product = reviews.merge(
    order_items[
        [
            "order_id",
            "product_id"
        ]
    ],
    on="order_id",
    how="left"
)

review_product = review_product.merge(
    products[
        [
            "product_id",
            "product_category_name_english"
        ]
    ],
    on="product_id",
    how="left"
)

product_ratings = (
    review_product
    .groupby("product_category_name_english")
    .agg(
        average_rating=("review_score", "mean"),
        review_count=("review_score", "count")
    )
    .reset_index()
    .sort_values(
        "average_rating",
        ascending=False
    )
)


# ==========================================
# 7. DISPLAY RESULTS
# ==========================================

print("===== PRODUCT ANALYSIS =====")

print("\nTotal Unique Products Sold:")
print(product_sales["product_id"].nunique())

print("\nTop 10 Product Categories by Sales:")
print(
    category_summary[
        [
            "product_category_name_english",
            "units_sold",
            "total_sales",
            "unique_products"
        ]
    ].head(10)
)


print("\nTop 10 Products by Sales:")
print(
    product_summary
    .sort_values(
        "total_sales",
        ascending=False
    )
    .head(10)
)


print("\nTop 10 Categories by Average Rating:")
print(
    product_ratings.head(10)
)


# ==========================================
# 8. SAVE ANALYSIS FILES
# ==========================================

product_summary.to_csv(
    "data/cleaned/product_summary.csv",
    index=False
)

category_summary.to_csv(
    "data/cleaned/category_summary.csv",
    index=False
)

product_ratings.to_csv(
    "data/cleaned/product_ratings.csv",
    index=False
)


print("\nProduct analysis completed!")
print("Product summary saved successfully!")
print("Category summary saved successfully!")
print("Product ratings saved successfully!")