import sqlite3

conn = sqlite3.connect('beauty.db')
cursor = conn.cursor()

cursor.execute('''SELECT id, name, brand, category, price FROM products 
                  WHERE brand IN ("Dot & Key", "Minimalist", "Swiss Beauty", "Faces Canada", 
                  "Maybelline", "Forever52", "Foxtale", "Aasaya", "Insight", "Mars", 
                  "L'Oreal Paris", "Streax", "Lakme") LIMIT 20''')
rows = cursor.fetchall()

print('Sample of added products:')
print('-' * 100)
for row in rows:
    print(f'ID: {row[0]}, Name: {row[1][:50]}, Brand: {row[2]}, Category: {row[3]}, Price: ₹{row[4]}')

cursor.execute('''SELECT brand, COUNT(*) FROM products 
                  WHERE brand IN ("Dot & Key", "Minimalist", "Swiss Beauty", "Faces Canada", 
                  "Maybelline", "Forever52", "Foxtale", "Aasaya", "Insight", "Mars", 
                  "L'Oreal Paris", "Streax", "Lakme") GROUP BY brand''')
print('\n' + '-' * 100)
print('Products per brand:')
for row in cursor.fetchall():
    print(f'{row[0]}: {row[1]} products')

conn.close()
