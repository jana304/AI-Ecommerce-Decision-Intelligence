import pandas as pd
import mysql.connector

# Load cleaned orders CSV
file_path = "data/cleaned/cleaned_orders.csv"
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
INSERT INTO orders (
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date,
    delivery_days,
    delivery_delay_days
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert missing values (NaN) to MySQL NULL
data = []

for row in df.itertuples(index=False):
    data.append((
        row.order_id,
        row.customer_id,
        row.order_status,
        None if pd.isna(row.order_purchase_timestamp) else row.order_purchase_timestamp,
        None if pd.isna(row.order_approved_at) else row.order_approved_at,
        None if pd.isna(row.order_delivered_carrier_date) else row.order_delivered_carrier_date,
        None if pd.isna(row.order_delivered_customer_date) else row.order_delivered_customer_date,
        None if pd.isna(row.order_estimated_delivery_date) else row.order_estimated_delivery_date,
        None if pd.isna(row.delivery_days) else row.delivery_days,
        None if pd.isna(row.delivery_delay_days) else row.delivery_delay_days
    ))

# Insert data
cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} orders inserted successfully.")

# Close connection
cursor.close()
connection.close()