import pandas as pd
import mysql.connector

# Load cleaned reviews CSV
file_path = "data/cleaned/cleaned_reviews.csv"
df = pd.read_csv(file_path)

# Remove duplicate review IDs
df = df.drop_duplicates(subset=["review_id"], keep="first")

print(f"Unique reviews to load: {len(df)}")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

# Insert reviews
# INSERT IGNORE skips duplicate review IDs
sql = """
INSERT IGNORE INTO reviews (
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message,
    review_creation_date,
    review_answer_timestamp
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Prepare data
data = []

for row in df.itertuples(index=False):
    data.append((
        row.review_id,
        row.order_id,
        int(row.review_score),
        row.review_comment_title,
        row.review_comment_message,
        None if pd.isna(row.review_creation_date) else row.review_creation_date,
        None if pd.isna(row.review_answer_timestamp) else row.review_answer_timestamp
    ))

# Insert into MySQL
cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} reviews inserted successfully.")

# Close connection
cursor.close()
connection.close()