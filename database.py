import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mydata.db')
print("Opened database successfully")

# Create a cursor object
cursor = conn.cursor()

# Create the table using a raw SQL statement
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")


# Create the teachers table with a different schema
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    subject_id TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
# Commit the changes and close the connection
conn.commit()
print("Table has been created")

conn.close()