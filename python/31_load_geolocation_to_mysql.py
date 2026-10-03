import pandas as pd
import mysql.connector

file_path = "data/cleaned/cleaned_geolocation.csv"
df = pd.read_csv(file_path)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="30405",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

sql = """
INSERT IGNORE INTO geolocation (
    geolocation_zip_code_prefix,
    geolocation_lat,
    geolocation_lng,
    geolocation_city,
    geolocation_state
)
VALUES (%s, %s, %s, %s, %s)
"""

data = []

for row in df.itertuples(index=False):
    data.append((
        int(row.geolocation_zip_code_prefix),
        None if pd.isna(row.geolocation_lat) else row.geolocation_lat,
        None if pd.isna(row.geolocation_lng) else row.geolocation_lng,
        row.geolocation_city,
        row.geolocation_state
    ))

cursor.executemany(sql, data)
connection.commit()

print(f"{cursor.rowcount} geolocation records inserted successfully.")

cursor.close()
connection.close()