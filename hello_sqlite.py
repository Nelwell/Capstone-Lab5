import sqlite3

conn = sqlite3.connect('first_db.sqlite')  # connect or create new if doesn't exist

conn.execute('CREATE TABLE products (id int, name text)')

conn.execute('INSERT INTO products values (1000, "hat")')  # add products
conn.execute('INSERT INTO products values (1001, "jacket")')

conn.commit()  # save changes, nothing finalized until committed

results = conn.execute('SELECT * FROM products')

for row in results:
    print(row)


conn.close()
