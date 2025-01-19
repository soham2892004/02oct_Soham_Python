import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Insert data into the table
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Ram', 30))
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Lakshaman', 25))
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bharat', 35))
c.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Shatrughna',29))
conn.commit()

# Fetch data from the table
c.execute('SELECT * FROM users')
rows = c.fetchall()

# Display the fetched data
for row in rows:
    print(row)

# Close the connection
conn.close()
