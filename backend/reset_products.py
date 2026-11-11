from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product

db = SessionLocal()

db.query(Product).delete()
db.commit()

products = [
    {"name": "Moisturizing Face Cream", "price": 29.99, "category": "Skincare", "brand": "GlowSkin", "image_url": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400", "description": "Hydrating daily face cream"},
    {"name": "Vitamin C Serum", "price": 39.99, "category": "Skincare", "brand": "RadiantGlow", "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400", "description": "Brightening vitamin C serum"},
    {"name": "Matte Lipstick", "price": 18.99, "category": "Makeup", "brand": "ColorPop", "image_url": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400", "description": "Long-lasting matte lipstick"},
    {"name": "Eyeshadow Palette", "price": 45.99, "category": "Makeup", "brand": "GlamourEyes", "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400", "description": "12-color eyeshadow palette"},
    {"name": "Hydrating Shampoo", "price": 24.99, "category": "Haircare", "brand": "SilkHair", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400", "description": "Moisturizing shampoo for dry hair"},
    {"name": "Hair Conditioner", "price": 24.99, "category": "Haircare", "brand": "SilkHair", "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400", "description": "Deep conditioning treatment"},
    {"name": "Floral Perfume", "price": 65.99, "category": "Fragrance", "brand": "Essence", "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "description": "Elegant floral fragrance"},
    {"name": "Body Lotion", "price": 19.99, "category": "Bodycare", "brand": "SoftTouch", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "description": "Nourishing body lotion"},
    {"name": "Face Mask Set", "price": 34.99, "category": "Skincare", "brand": "PureGlow", "image_url": "https://images.unsplash.com/photo-1608248597279-f99d160bfcbc?w=400", "description": "5-pack hydrating face masks"},
    {"name": "Nail Polish Set", "price": 22.99, "category": "Makeup", "brand": "ColorNails", "image_url": "https://images.unsplash.com/photo-1519823551278-64ac92734fb1?w=400", "description": "6-color nail polish collection"},
]

for p in products:
    product = Product(**p, stock=100)
    db.add(product)

db.commit()
print(f"Added {len(products)} products with images, names, and prices")
db.close()
