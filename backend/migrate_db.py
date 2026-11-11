"""
Database migration script to add shipping and payment columns to orders table
"""
import sqlite3

def migrate():
    conn = sqlite3.connect('beauty.db')
    cursor = conn.cursor()
    
    # Check if columns already exist
    cursor.execute("PRAGMA table_info(orders)")
    columns = [col[1] for col in cursor.fetchall()]
    
    # Add new columns if they don't exist
    new_columns = [
        ('shipping_fullname', 'TEXT'),
        ('shipping_mobile', 'TEXT'),
        ('shipping_city', 'TEXT'),
        ('shipping_pincode', 'TEXT'),
        ('shipping_state', 'TEXT'),
        ('payment_method', 'TEXT'),
        ('payment_id', 'TEXT')
    ]
    
    for col_name, col_type in new_columns:
        if col_name not in columns:
            try:
                cursor.execute(f"ALTER TABLE orders ADD COLUMN {col_name} {col_type}")
                print(f"✅ Added column: {col_name}")
            except sqlite3.OperationalError as e:
                print(f"⚠️  Column {col_name} might already exist: {e}")
    
    conn.commit()
    conn.close()
    print("✅ Migration completed!")

if __name__ == "__main__":
    migrate()
