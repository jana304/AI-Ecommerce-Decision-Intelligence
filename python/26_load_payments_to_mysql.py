import pandas as pd
import mysql.connector

file_path = "data/cleaned/cleaned_payments.csv"
df = pd.read_csv(file_path)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

sql = """
INSERT INTO payments (
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
)
VALUES (%s, %s, %s, %s, %s)
"""

data = []

for row in df.itertuples(index=False):
    data.append((
        row.order_id,
        int(row.payment_sequential),
        row.payment_type,
        int(row.payment_installments),
        None if pd.isna(row.payment_value) else row.payment_value
    ))

cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} payments inserted successfully.")

cursor.close()
connection.close()