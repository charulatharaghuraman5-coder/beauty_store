from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

new_products = [
    # Skincare
    {"name": "Hyaluronic Acid Serum", "description": "Deep hydration serum with pure hyaluronic acid", "price": 799, "category": "Skincare", "brand": "The Ordinary", "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400", "stock": 50},
    {"name": "Retinol Night Cream", "description": "Anti-aging night cream with retinol", "price": 1299, "category": "Skincare", "brand": "Olay", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 40},
    {"name": "Vitamin E Face Cream", "description": "Nourishing face cream with vitamin E", "price": 599, "category": "Skincare", "brand": "Nivea", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 60},
    {"name": "Charcoal Face Mask", "description": "Deep cleansing charcoal peel-off mask", "price": 399, "category": "Skincare", "brand": "Mamaearth", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 70},
    {"name": "Aloe Vera Gel", "description": "Pure aloe vera gel for skin and hair", "price": 249, "category": "Skincare", "brand": "Patanjali", "image_url": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400", "stock": 100},
    
    # Makeup
    {"name": "HD Pro Foundation", "description": "High definition liquid foundation", "price": 899, "category": "Makeup", "brand": "MAC", "image_url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400", "stock": 45},
    {"name": "Matte Liquid Lipstick", "description": "Long-lasting matte liquid lipstick", "price": 599, "category": "Makeup", "brand": "Huda Beauty", "image_url": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400", "stock": 80},
    {"name": "Eyebrow Pencil", "description": "Waterproof eyebrow pencil", "price": 299, "category": "Makeup", "brand": "Maybelline", "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400", "stock": 90},
    {"name": "Compact Powder", "description": "Oil-control compact powder", "price": 449, "category": "Makeup", "brand": "Lakme", "image_url": "https://images.unsplash.com/photo-1596704017254-9b121068ec31?w=400", "stock": 70},
    {"name": "Eyeliner Pen", "description": "Waterproof black eyeliner pen", "price": 349, "category": "Makeup", "brand": "Maybelline", "image_url": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400", "stock": 85},
    
    # Haircare
    {"name": "Argan Oil Hair Serum", "description": "Nourishing argan oil for smooth hair", "price": 699, "category": "Haircare", "brand": "Moroccan Oil", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400", "stock": 55},
    {"name": "Anti-Dandruff Shampoo", "description": "Clinically proven anti-dandruff formula", "price": 399, "category": "Haircare", "brand": "Head & Shoulders", "image_url": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400", "stock": 75},
    {"name": "Hair Growth Oil", "description": "Ayurvedic hair growth oil", "price": 499, "category": "Haircare", "brand": "Kesh King", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400", "stock": 65},
    {"name": "Deep Conditioning Mask", "description": "Intensive repair hair mask", "price": 799, "category": "Haircare", "brand": "L'Oreal", "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400", "stock": 50},
    {"name": "Hair Straightening Cream", "description": "Keratin-infused straightening cream", "price": 599, "category": "Haircare", "brand": "Streax", "image_url": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400", "stock": 60},
    
    # Fragrance
    {"name": "Rose Eau de Parfum", "description": "Romantic rose fragrance for women", "price": 1499, "category": "Fragrance", "brand": "Chanel", "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "stock": 30},
    {"name": "Oud Perfume", "description": "Luxurious oud fragrance", "price": 1899, "category": "Fragrance", "brand": "Ajmal", "image_url": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400", "stock": 25},
    {"name": "Citrus Body Mist", "description": "Refreshing citrus body spray", "price": 399, "category": "Fragrance", "brand": "Bath & Body Works", "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "stock": 70},
    {"name": "Lavender Perfume", "description": "Calming lavender fragrance", "price": 899, "category": "Fragrance", "brand": "Forest Essentials", "image_url": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400", "stock": 45},
    {"name": "Musk Attar", "description": "Traditional musk attar", "price": 699, "category": "Fragrance", "brand": "Zara", "image_url": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400", "stock": 55},
    
    # Bath and Body
    {"name": "Shea Butter Body Lotion", "description": "Ultra-moisturizing shea butter lotion", "price": 599, "category": "Bath and Body", "brand": "The Body Shop", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 60},
    {"name": "Coffee Body Scrub", "description": "Exfoliating coffee scrub", "price": 449, "category": "Bath and Body", "brand": "mCaffeine", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 70},
    {"name": "Rose Bath Bombs", "description": "Fizzing rose-scented bath bombs", "price": 399, "category": "Bath and Body", "brand": "Lush", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 50},
    {"name": "Coconut Body Butter", "description": "Rich coconut body butter", "price": 699, "category": "Bath and Body", "brand": "Palmer's", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 55},
    {"name": "Lavender Hand Cream", "description": "Soothing lavender hand cream", "price": 299, "category": "Bath and Body", "brand": "L'Occitane", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 80},
]

for product_data in new_products:
    product = models.Product(**product_data)
    db.add(product)

db.commit()
print(f"✅ Added {len(new_products)} new products to the database")
print(f"✅ Total products: {db.query(models.Product).count()}")
db.close()
