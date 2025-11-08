import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    body TEXT
)
''')

# seed with small sample data
c.execute("DELETE FROM posts")
c.executemany("INSERT INTO posts (title, body) VALUES (?, ?)", [
    ("Hello World", "This is the first post"),
    ("About SQL", "SQL is powerful"),
    ("Contact", "Contact us at contact@example.com"),
])
conn.commit()
conn.close()
print("Initialized database with sample data.")
