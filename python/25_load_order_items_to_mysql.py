import pandas as pd
import mysql.connector

# Load cleaned order items CSV
file_path = "data/cleaned/cleaned_order_items.csv"
df = pd.read_csv(file_path)

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

# SQL insert statement
sql = """
INSERT INTO order_items (
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value,
    total_item_value
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert missing values to MySQL NULL
data = []

for row in df.itertuples(index=False):
    data.append((
        row.order_id,
        int(row.order_item_id),
        row.product_id,
        row.seller_id,
        None if pd.isna(row.shipping_limit_date) else row.shipping_limit_date,
        None if pd.isna(row.price) else row.price,
        None if pd.isna(row.freight_value) else row.freight_value,
        None if pd.isna(row.total_item_value) else row.total_item_value
    ))

# Insert data
cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} order items inserted successfully.")

# Close connection
cursor.close()
connection.close()