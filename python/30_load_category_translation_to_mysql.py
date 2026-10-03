import pandas as pd
import mysql.connector

file_path = "data/cleaned/cleaned_category_translation.csv"
df = pd.read_csv(file_path)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

sql = """
INSERT IGNORE INTO category_translation (
    product_category_name,
    product_category_name_english
)
VALUES (%s, %s)
"""

data = []

for row in df.itertuples(index=False):
    data.append((
        row.product_category_name,
        row.product_category_name_english
    ))

cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} categories inserted successfully.")

cursor.close()
connection.close()