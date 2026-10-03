import pandas as pd
import mysql.connector

# Load cleaned customer data
file_path = "data/cleaned/cleaned_customers.csv"
df = pd.read_csv(file_path)

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

# Insert data
sql = """
INSERT INTO customers (
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state
)
VALUES (%s, %s, %s, %s, %s)
"""

data = [
    (
        row.customer_id,
        row.customer_unique_id,
        int(row.customer_zip_code_prefix),
        row.customer_city,
        row.customer_state
    )
    for row in df.itertuples(index=False)
]

cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} customers inserted successfully.")

cursor.close()
connection.close()