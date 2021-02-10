import sqlite3

conn = sqlite3.connect('first_db.sqlite')  # connect or create new if doesn't exist
# conn.row_factory = sqlite3.Row

conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')

conn.execute('INSERT INTO products values (1000, "hat")')  # add products
conn.execute('INSERT INTO products values (1001, "jacket")')

conn.commit()  # save changes, nothing finalized until committed

results = conn.execute('SELECT * FROM products')

all_rows = results.fetchall()
print(all_rows)

for row in results:
    print(row[1])  # each row is a tuple, row object
    # print(row['name'])

results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
first_row = results.fetchone()
print(first_row)

# new_id = int(input('enter new id: '))
# new_name = input('enter new product: ')
#
# conn.execute(f'INSERT INTO products VALUES(?, ?)', (new_id, new_name))
# conn.commit()

updated_product = 'wool hat'
update_id = 1000
conn.execute('UPDATE products SET name = ? WHERE id = ? ', (updated_product, update_id))
conn.commit()

delete_product = 'jacket'
conn.execute('DELETE from PRODUCTS WHERE name = ?', (delete_product, ))
conn.commit()

conn.close()
