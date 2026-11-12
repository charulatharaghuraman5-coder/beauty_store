from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Product

Base.metadata.create_all(bind=engine)

def add_real_brand_products():
    db = SessionLocal()
    
    # Clear existing products
    db.query(Product).delete()
    
    products = [
        # Dot & Key
        Product(name="Vitamin C + E Serum", brand="Dot & Key", price=899, category="Skincare", 
                description="Brightening serum with 10% Vitamin C", stock=50,
                image_url="https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400"),
        Product(name="Watermelon Cooling Gel", brand="Dot & Key", price=599, category="Skincare",
                description="Hydrating gel for all skin types", stock=60,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        
        # Lakme
        Product(name="9 to 5 Primer + Matte Lipstick", brand="Lakme", price=475, category="Makeup",
                description="Long-lasting matte lipstick", stock=100,
                image_url="https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"),
        Product(name="Absolute Skin Natural Mousse", brand="Lakme", price=650, category="Makeup",
                description="Lightweight foundation", stock=45,
                image_url="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400"),
        Product(name="Eyeconic Kajal", brand="Lakme", price=225, category="Makeup",
                description="Smudge-proof kajal", stock=150,
                image_url="https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"),
        
        # Forever52
        Product(name="Matte Liquid Lipstick", brand="Forever52", price=399, category="Makeup",
                description="High pigment matte finish", stock=80,
                image_url="https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"),
        Product(name="Eyeshadow Palette", brand="Forever52", price=799, category="Makeup",
                description="12 shade eyeshadow palette", stock=40,
                image_url="https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"),
        
        # Swiss Beauty
        Product(name="HD Foundation", brand="Swiss Beauty", price=349, category="Makeup",
                description="Full coverage foundation", stock=70,
                image_url="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400"),
        Product(name="Baked Highlighter", brand="Swiss Beauty", price=299, category="Makeup",
                description="Shimmer highlighter", stock=90,
                image_url="https://images.unsplash.com/photo-1596704017254-9b121068ec31?w=400"),
        
        # Faces Canada
        Product(name="Ultime Pro HD Intense Matte Lips", brand="Faces Canada", price=599, category="Makeup",
                description="Transfer-proof liquid lipstick", stock=65,
                image_url="https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"),
        Product(name="Magneteyes Kajal", brand="Faces Canada", price=349, category="Makeup",
                description="Intense black kajal", stock=120,
                image_url="https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400"),
        
        # L'Oreal Paris
        Product(name="Revitalift Crystal Micro-Essence", brand="L'Oreal Paris", price=1299, category="Skincare",
                description="Anti-aging essence", stock=35,
                image_url="https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400"),
        Product(name="Infallible Pro-Matte Foundation", brand="L'Oreal Paris", price=1050, category="Makeup",
                description="24H matte foundation", stock=55,
                image_url="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400"),
        Product(name="Color Riche Matte Lipstick", brand="L'Oreal Paris", price=850, category="Makeup",
                description="Rich matte lipstick", stock=75,
                image_url="https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"),
        
        # Streax
        Product(name="Hair Serum", brand="Streax", price=299, category="Haircare",
                description="Smoothing hair serum", stock=100,
                image_url="https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400"),
        Product(name="Professional Hair Color", brand="Streax", price=149, category="Haircare",
                description="Ammonia-free hair color", stock=85,
                image_url="https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=400"),
        
        # Insight
        Product(name="Damage Hair Restructurizing Shampoo", brand="Insight", price=850, category="Haircare",
                description="Professional hair repair", stock=40,
                image_url="https://images.unsplash.com/photo-1571875257727-256c39da42af?w=400"),
        
        # Foxtale
        Product(name="Daily Duet Sunscreen SPF 50", brand="Foxtale", price=699, category="Skincare",
                description="Broad spectrum sunscreen", stock=60,
                image_url="https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400"),
        Product(name="Hydrating Face Wash", brand="Foxtale", price=449, category="Skincare",
                description="Gentle daily cleanser", stock=80,
                image_url="https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400"),
        
        # Aqualogica
        Product(name="Glow+ Dewy Sunscreen SPF 50", brand="Aqualogica", price=499, category="Skincare",
                description="Hydrating sunscreen", stock=70,
                image_url="https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400"),
        
        # Laneige
        Product(name="Water Sleeping Mask", brand="Laneige", price=2450, category="Skincare",
                description="Overnight hydrating mask", stock=30,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Lip Sleeping Mask", brand="Laneige", price=1650, category="Skincare",
                description="Overnight lip treatment", stock=45,
                image_url="https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"),
        
        # Derma Co
        Product(name="2% Salicylic Acid Face Wash", brand="Derma Co", price=399, category="Skincare",
                description="Acne control cleanser", stock=90,
                image_url="https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400"),
        Product(name="10% Niacinamide Serum", brand="Derma Co", price=599, category="Skincare",
                description="Pore minimizing serum", stock=75,
                image_url="https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400"),
        
        # Nivea
        Product(name="Soft Light Moisturizer SPF 30", brand="Nivea", price=299, category="Skincare",
                description="Daily moisturizer with SPF", stock=110,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Lip Balm Cherry Shine", brand="Nivea", price=149, category="Skincare",
                description="Moisturizing lip balm", stock=150,
                image_url="https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"),
        Product(name="Body Lotion Nourishing", brand="Nivea", price=349, category="Bodycare",
                description="48h deep moisture", stock=95,
                image_url="https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400"),
    ]
    
    db.add_all(products)
    db.commit()
    print(f"✅ Added {len(products)} real brand products!")
    db.close()

if __name__ == "__main__":
    add_real_brand_products()
