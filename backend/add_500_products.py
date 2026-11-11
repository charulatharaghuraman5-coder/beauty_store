from database import SessionLocal
from models import Product
import random

db = SessionLocal()

categories = {
    "Makeup": ["Lipstick", "Foundation", "Mascara", "Eyeshadow", "Blush", "Eyeliner", "Concealer", "Highlighter", "Bronzer", "Lip Gloss"],
    "Skincare": ["Face Serum", "Moisturizer", "Cleanser", "Toner", "Face Mask", "Eye Cream", "Sunscreen", "Night Cream", "Face Oil", "Exfoliator"],
    "Fragrance": ["Perfume", "Body Mist", "Eau de Toilette", "Cologne", "Fragrance Oil", "Roll-on Perfume", "Solid Perfume", "Hair Mist", "Body Spray", "Scented Lotion"],
    "Bath and Body": ["Body Lotion", "Body Wash", "Body Scrub", "Bath Bomb", "Body Butter", "Hand Cream", "Foot Cream", "Body Oil", "Shower Gel", "Bath Salts"]
}

brands = ["Lakme", "Maybelline", "L'Oreal", "MAC", "Nykaa", "Colorbar", "Revlon", "Clinique", "Estee Lauder", "Bobbi Brown", "Huda Beauty", "Fenty Beauty", "Dior", "Chanel", "YSL", "Urban Decay", "Benefit", "Too Faced", "Anastasia", "Tarte"]

products_added = 0

for category, product_types in categories.items():
    for i in range(125):
        product_type = random.choice(product_types)
        brand = random.choice(brands)
        price = round(random.uniform(299, 4999), 2)
        
        product = Product(
            name=f"{brand} {product_type} {i+1}",
            description=f"Premium {product_type.lower()} from {brand}. Long-lasting, high-quality formula.",
            price=price,
            category=category,
            brand=brand,
            image_url=f"https://via.placeholder.com/250?text={brand}+{product_type}",
            stock=random.randint(10, 100)
        )
        db.add(product)
        products_added += 1

db.commit()
print(f"✅ Added {products_added} products!")
db.close()
