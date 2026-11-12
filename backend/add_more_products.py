from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product

def add_more_products():
    db = SessionLocal()
    
    new_products = [
        # Fragrance - Real Brands
        Product(name="Yardley London Gentleman Eau de Parfum", brand="Yardley", price=599, category="Fragrance",
                description="Classic masculine fragrance", stock=45,
                image_url="https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400"),
        Product(name="Engage W1 Perfume Spray", brand="Engage", price=299, category="Fragrance",
                description="Long-lasting perfume for women", stock=60,
                image_url="https://images.unsplash.com/photo-1541643600914-78b084683601?w=400"),
        Product(name="Wild Stone Code Titanium Perfume", brand="Wild Stone", price=399, category="Fragrance",
                description="Bold and intense fragrance", stock=55,
                image_url="https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400"),
        Product(name="Bella Vita Luxury CEO Man Perfume", brand="Bella Vita", price=449, category="Fragrance",
                description="Premium luxury perfume", stock=40,
                image_url="https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400"),
        Product(name="Skinn by Titan Celeste Eau de Parfum", brand="Skinn by Titan", price=1299, category="Fragrance",
                description="Elegant floral fragrance", stock=30,
                image_url="https://images.unsplash.com/photo-1541643600914-78b084683601?w=400"),
        Product(name="Park Avenue Storm Deodorant", brand="Park Avenue", price=199, category="Fragrance",
                description="Fresh deodorant spray", stock=80,
                image_url="https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400"),
        Product(name="Fogg Scent Xpressio Fragrance", brand="Fogg", price=249, category="Fragrance",
                description="Long-lasting body spray", stock=70,
                image_url="https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400"),
        Product(name="Denver Hamilton Deodorant", brand="Denver", price=175, category="Fragrance",
                description="Classic masculine deo", stock=90,
                image_url="https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=400"),
        
        # Bath & Body - Real Brands
        Product(name="Dove Deeply Nourishing Body Wash", brand="Dove", price=349, category="Bath and Body",
                description="Moisturizing body wash", stock=75,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="The Body Shop Vitamin E Body Butter", brand="The Body Shop", price=1695, category="Bath and Body",
                description="Intense moisture body butter", stock=35,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Vaseline Intensive Care Body Lotion", brand="Vaseline", price=299, category="Bath and Body",
                description="Deep restore body lotion", stock=85,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Himalaya Nourishing Body Lotion", brand="Himalaya", price=195, category="Bath and Body",
                description="Natural body moisturizer", stock=95,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Neutrogena Deep Moisture Body Lotion", brand="Neutrogena", price=599, category="Bath and Body",
                description="24h hydration lotion", stock=50,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Palmolive Naturals Shower Gel", brand="Palmolive", price=249, category="Bath and Body",
                description="Refreshing shower gel", stock=70,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Fiama Di Wills Gel Bar", brand="Fiama", price=99, category="Bath and Body",
                description="Skin conditioning gel bar", stock=100,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Lux Velvet Touch Body Wash", brand="Lux", price=299, category="Bath and Body",
                description="Luxurious body wash", stock=80,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Pears Pure & Gentle Body Wash", brand="Pears", price=249, category="Bath and Body",
                description="Gentle cleansing body wash", stock=75,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
        Product(name="Biotique Bio Honey Gel Body Wash", brand="Biotique", price=299, category="Bath and Body",
                description="Natural honey body wash", stock=65,
                image_url="https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"),
    ]
    
    db.add_all(new_products)
    db.commit()
    print(f"✅ Added {len(new_products)} more products!")
    print("\nFragrance products:")
    for p in new_products[:8]:
        print(f"  {p.brand} - {p.name} - ₹{p.price}")
    print("\nBath & Body products:")
    for p in new_products[8:]:
        print(f"  {p.brand} - {p.name} - ₹{p.price}")
    
    db.close()

if __name__ == "__main__":
    add_more_products()
