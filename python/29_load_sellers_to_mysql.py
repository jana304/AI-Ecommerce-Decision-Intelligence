import pandas as pd
import mysql.connector

file_path = "data/cleaned/cleaned_sellers.csv"
df = pd.read_csv(file_path)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

sql = """
INSERT IGNORE INTO sellers (
    seller_id,
    seller_zip_code_prefix,
    seller_city,
    seller_state
)
VALUES (%s, %s, %s, %s)
"""

data = []

for row in df.itertuples(index=False):
    data.append((
        row.seller_id,
        int(row.seller_zip_code_prefix),
        row.seller_city,
        row.seller_state
    ))

cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} sellers inserted successfully.")

cursor.close()
connection.close()