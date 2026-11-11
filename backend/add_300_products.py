import sqlite3
import random

brands = ['Dot & Key', 'Minimalist', 'Swiss Beauty', 'Faces Canada', 'Maybelline', 'Forever52', 'Foxtale', 'Aasaya', 'Insight', 'Mars', 'L\'Oreal Paris', 'Streax', 'Lakme']

products_by_category = {
    'Skincare': ['Vitamin C Serum', 'Niacinamide Serum', 'Hyaluronic Acid Serum', 'Retinol Serum', 'Face Wash', 'Gel Cleanser', 'Foaming Cleanser', 'Micellar Water', 'Night Cream', 'Day Cream', 'Moisturizer', 'Sunscreen SPF 50', 'Sunscreen SPF 30', 'Under Eye Cream', 'Face Mask', 'Sheet Mask', 'Clay Mask', 'Peel Off Mask', 'Toner', 'Face Mist', 'Exfoliator', 'Face Scrub', 'Lip Balm', 'Sleeping Mask', 'Essence', 'Face Oil', 'Acne Gel', 'Spot Corrector'],
    'Makeup': ['Matte Lipstick', 'Liquid Lipstick', 'Lip Crayon', 'Lip Gloss', 'Lip Tint', 'Foundation', 'Compact Powder', 'BB Cream', 'CC Cream', 'Concealer', 'Primer', 'Setting Spray', 'Blush', 'Highlighter', 'Bronzer', 'Contour Stick', 'Eyeshadow Palette', 'Kajal', 'Eyeliner', 'Mascara', 'Eyebrow Pencil', 'Brow Gel', 'Nail Polish', 'Nail Enamel', 'Makeup Remover', 'Fixing Powder'],
    'Haircare': ['Shampoo', 'Conditioner', 'Hair Serum', 'Hair Oil', 'Hair Mask', 'Hair Spa Cream', 'Anti-Dandruff Shampoo', 'Hair Color', 'Hair Dye', 'Hair Straightening Cream', 'Hair Gel', 'Hair Wax', 'Hair Spray', 'Leave-in Conditioner', 'Dry Shampoo', 'Hair Growth Oil', 'Scalp Scrub', 'Hair Mousse'],
    'Bath and Body': ['Body Lotion', 'Body Butter', 'Body Wash', 'Shower Gel', 'Body Scrub', 'Hand Cream', 'Foot Cream', 'Body Mist', 'Deodorant', 'Perfume', 'Body Oil', 'Bath Salt', 'Soap', 'Hand Wash', 'Body Spray'],
    'Fragrance': ['Eau De Parfum', 'Eau De Toilette', 'Perfume', 'Body Mist', 'Deodorant Spray', 'Roll-on Deodorant', 'Pocket Perfume', 'Fragrance Gift Set']
}

adjectives = ['Radiant', 'Glow', 'Matte', 'Shimmer', 'Velvet', 'Satin', 'Silk', 'Ultra', 'Pro', 'HD', 'Long Lasting', 'Waterproof', 'Smudge Proof', '24HR', 'Intense', 'Natural', 'Nude', 'Bold', 'Vivid', 'Pure', 'Fresh', 'Hydrating', 'Nourishing', 'Brightening', 'Anti-Aging', 'Deep', 'Gentle', 'Luxury', 'Professional']

images = [
    "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400",
    "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400",
    "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400",
    "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400",
    "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400",
    "https://images.unsplash.com/photo-1583241800698-c318c76ca7e6?w=400",
    "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400",
    "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400",
    "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400",
    "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400"
]

conn = sqlite3.connect('beauty.db')
cursor = conn.cursor()

cursor.execute("SELECT MAX(id) FROM products")
max_id = cursor.fetchone()[0] or 0
id_counter = max_id + 1

products_to_add = []
for _ in range(300):
    brand = random.choice(brands)
    category = random.choice(list(products_by_category.keys()))
    product_base = random.choice(products_by_category[category])
    adj = random.choice(adjectives)
    name = f"{brand} {adj} {product_base}"
    price = round(random.uniform(199, 2499), 2)
    image = random.choice(images)
    stock = random.randint(50, 200)
    description = f"Premium {product_base.lower()} from {brand}"
    
    products_to_add.append((id_counter, name, description, price, category, brand, image, stock))
    id_counter += 1

cursor.executemany(
    "INSERT INTO products (id, name, description, price, category, brand, image_url, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    products_to_add
)

conn.commit()
print(f"Successfully added {len(products_to_add)} products!")
conn.close()
