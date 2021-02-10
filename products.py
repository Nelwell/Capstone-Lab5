import sqlite3

# validation errors, rowid

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS products (name TEXT UNIQUE, quantity INT)')
conn.close()

name = 'hat'
quantity = 4

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (?, ?)', (name, quantity))
    conn.close()
except Exception as e:
    print('Error inserting ', e)

conn = sqlite3.connect(db)
results = conn.execute('SELECT rowid, * FROM products')
for row in results:
    print(row)

print('End of program!')
