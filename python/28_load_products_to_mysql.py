import pandas as pd
import mysql.connector

# Load cleaned products CSV
file_path = "data/cleaned/cleaned_products.csv"
df = pd.read_csv(file_path)

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

sql = """
INSERT IGNORE INTO products (
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

data = []

for row in df.itertuples(index=False):
    data.append((
        row.product_id,
        row.product_category_name,
        None if pd.isna(row.product_name_lenght) else int(row.product_name_lenght),
        None if pd.isna(row.product_description_lenght) else int(row.product_description_lenght),
        None if pd.isna(row.product_photos_qty) else int(row.product_photos_qty),
        None if pd.isna(row.product_weight_g) else row.product_weight_g,
        None if pd.isna(row.product_length_cm) else row.product_length_cm,
        None if pd.isna(row.product_height_cm) else row.product_height_cm,
        None if pd.isna(row.product_width_cm) else row.product_width_cm
    ))

cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} products inserted successfully.")

cursor.close()
connection.close()