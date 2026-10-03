import pandas as pd

# Load raw reviews
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")

# Convert date columns
reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)

reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
)

# Fill missing comments with a clear label
reviews["review_comment_title"] = reviews["review_comment_title"].fillna(
    "No comment"
)

reviews["review_comment_message"] = reviews["review_comment_message"].fillna(
    "No comment"
)

print("Reviews cleaned successfully!")
print("Rows:", len(reviews))
print("Columns:", len(reviews.columns))

print("\nMissing values:")
print(reviews.isnull().sum())

print("\nReview score distribution:")
print(reviews["review_score"].value_counts().sort_index())

# Save cleaned file
reviews.to_csv(
    "data/cleaned/cleaned_reviews.csv",
    index=False
)

print("\nCleaned reviews file saved successfully!")