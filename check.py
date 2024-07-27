import sqlite3
import os

# Use the same instance path as in your Flask app
db_path = '/home/val_vv/new_db.sqlite'  # Replace with your actual path

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Execute the query to select all columns from the user table
cursor.execute("SELECT * FROM user;")

# Fetch all rows
rows = cursor.fetchall()

# Print column names
print("Columns: ", [desc[0] for desc in cursor.description])

# Print each row
for row in rows:
    print(row)

# Close the connection
conn.close()
