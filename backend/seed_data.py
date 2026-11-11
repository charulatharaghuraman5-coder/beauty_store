from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

def seed_products():
    db = SessionLocal()
    
    existing_products = db.query(models.Product).count()
    if existing_products > 0:
        print("Database already has products. Skipping seed.")
        db.close()
        return
    
    sample_products = [
        # Skincare
        {
            "name": "Hydrating Face Serum",
            "description": "Intensive hydration serum with hyaluronic acid",
            "price": 1299.00,
            "category": "Skincare",
            "brand": "GlowLab",
            "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400",
            "stock": 50
        },
        {
            "name": "Vitamin C Brightening Cream",
            "description": "Brightening day cream with Vitamin C and SPF 30",
            "price": 899.00,
            "category": "Skincare",
            "brand": "RadiantSkin",
            "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400",
            "stock": 75
        },
        {
            "name": "Gentle Foaming Cleanser",
            "description": "pH balanced cleanser for all skin types",
            "price": 549.00,
            "category": "Skincare",
            "brand": "PureGlow",
            "image_url": "https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400",
            "stock": 100
        },
        
        # Makeup
        {
            "name": "Matte Liquid Lipstick",
            "description": "Long-lasting matte finish lipstick in Ruby Red",
            "price": 699.00,
            "category": "Makeup",
            "brand": "ColorPop",
            "image_url": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400",
            "stock": 120
        },
        {
            "name": "HD Foundation",
            "description": "Full coverage foundation with natural finish",
            "price": 1499.00,
            "category": "Makeup",
            "brand": "FlawlessBeauty",
            "image_url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400",
            "stock": 60
        },
        {
            "name": "Eyeshadow Palette",
            "description": "12 shade neutral eyeshadow palette",
            "price": 1899.00,
            "category": "Makeup",
            "brand": "GlamEyes",
            "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400",
            "stock": 45
        },
        
        # Haircare
        {
            "name": "Argan Oil Hair Serum",
            "description": "Nourishing hair serum with pure argan oil",
            "price": 799.00,
            "category": "Haircare",
            "brand": "SilkHair",
            "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400",
            "stock": 80
        },
        {
            "name": "Keratin Repair Shampoo",
            "description": "Strengthening shampoo for damaged hair",
            "price": 649.00,
            "category": "Haircare",
            "brand": "HairRevive",
            "image_url": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400",
            "stock": 90
        },
        
        # Fragrance
        {
            "name": "Rose Garden Perfume",
            "description": "Elegant floral fragrance with rose and jasmine",
            "price": 2499.00,
            "category": "Fragrance",
            "brand": "LuxeScent",
            "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400",
            "stock": 35
        },
        {
            "name": "Ocean Breeze EDT",
            "description": "Fresh aquatic fragrance for everyday wear",
            "price": 1799.00,
            "category": "Fragrance",
            "brand": "AquaEssence",
            "image_url": "https://images.unsplash.com/photo-1588405748880-12d1d2a59d75?w=400",
            "stock": 40
        },
        
        # Bath and Body
        {
            "name": "Lavender Body Lotion",
            "description": "Moisturizing body lotion with lavender extract",
            "price": 599.00,
            "category": "Bath and Body",
            "brand": "BodyBliss",
            "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400",
            "stock": 110
        },
        {
            "name": "Coconut Body Scrub",
            "description": "Exfoliating body scrub with coconut oil",
            "price": 749.00,
            "category": "Bath and Body",
            "brand": "TropicalGlow",
            "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400",
            "stock": 65
        }
    ]
    
    for product_data in sample_products:
        product = models.Product(**product_data)
        db.add(product)
    
    admin_user = models.User(
        email="admin@beauty.com",
        username="admin",
        hashed_password="$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/1jriu",
        full_name="Admin User",
        is_admin=True
    )
    db.add(admin_user)
    
    db.commit()
    print("✅ Database seeded successfully with sample products!")
    print("👤 Admin user created - Username: admin, Password: admin123")
    db.close()

if __name__ == "__main__":
    seed_products()
