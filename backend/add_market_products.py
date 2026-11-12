from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Product

Base.metadata.create_all(bind=engine)

def add_market_products():
    db = SessionLocal()
    
    # Clear existing products
    db.query(Product).delete()
    
    products = [
        # Dot & Key
        Product(name="Vitamin C + E Super Bright Serum", brand="Dot & Key", price=899, category="Skincare", 
                description="10% Vitamin C serum for brightening", stock=50,
                image_url="https://m.media-amazon.com/images/I/51VqN8YZPNL._SX679_.jpg"),
        Product(name="Watermelon Hyaluronic Cooling Gel", brand="Dot & Key", price=599, category="Skincare",
                description="72hr hydration gel moisturizer", stock=60,
                image_url="https://m.media-amazon.com/images/I/51xQqH7RKSL._SX679_.jpg"),
        
        # Lakme
        Product(name="9 to 5 Primer Matte Lipstick", brand="Lakme", price=475, category="Makeup",
                description="Long-lasting matte lipstick", stock=100,
                image_url="https://m.media-amazon.com/images/I/41VqYqH8pPL._SX679_.jpg"),
        Product(name="Absolute Skin Natural Mousse", brand="Lakme", price=650, category="Makeup",
                description="Lightweight mousse foundation", stock=45,
                image_url="https://m.media-amazon.com/images/I/41xN8YZPNL._SX679_.jpg"),
        Product(name="Eyeconic Kajal", brand="Lakme", price=225, category="Makeup",
                description="Smudge-proof black kajal", stock=150,
                image_url="https://m.media-amazon.com/images/I/51VqN8YZPNL._SX679_.jpg"),
        
        # L'Oreal Paris
        Product(name="Revitalift Crystal Micro-Essence", brand="L'Oreal Paris", price=1299, category="Skincare",
                description="Anti-aging face essence", stock=35,
                image_url="https://m.media-amazon.com/images/I/41xQqH7RKSL._SX679_.jpg"),
        Product(name="Infallible Pro-Matte Foundation", brand="L'Oreal Paris", price=1050, category="Makeup",
                description="24H matte finish foundation", stock=55,
                image_url="https://m.media-amazon.com/images/I/51VqYqH8pPL._SX679_.jpg"),
        Product(name="Color Riche Matte Lipstick", brand="L'Oreal Paris", price=850, category="Makeup",
                description="Rich matte lipstick", stock=75,
                image_url="https://m.media-amazon.com/images/I/41VqN8YZPNL._SX679_.jpg"),
        
        # Maybelline
        Product(name="Fit Me Matte Foundation", brand="Maybelline", price=499, category="Makeup",
                description="Natural matte foundation", stock=80,
                image_url="https://m.media-amazon.com/images/I/51xN8YZPNL._SX679_.jpg"),
        Product(name="SuperStay Matte Ink Lipstick", brand="Maybelline", price=699, category="Makeup",
                description="16hr liquid matte lipstick", stock=90,
                image_url="https://m.media-amazon.com/images/I/41xQqH7RKSL._SX679_.jpg"),
        Product(name="Colossal Kajal", brand="Maybelline", price=199, category="Makeup",
                description="Intense black kajal", stock=120,
                image_url="https://m.media-amazon.com/images/I/51VqN8YZPNL._SX679_.jpg"),
        
        # Nivea
        Product(name="Soft Light Moisturizer SPF 30", brand="Nivea", price=299, category="Skincare",
                description="Daily moisturizer with SPF", stock=110,
                image_url="https://m.media-amazon.com/images/I/51xQqH7RKSL._SX679_.jpg"),
        Product(name="Lip Balm Cherry Shine", brand="Nivea", price=149, category="Skincare",
                description="Moisturizing lip balm", stock=150,
                image_url="https://m.media-amazon.com/images/I/41VqYqH8pPL._SX679_.jpg"),
        Product(name="Body Lotion Nourishing", brand="Nivea", price=349, category="Bodycare",
                description="48h deep moisture lotion", stock=95,
                image_url="https://m.media-amazon.com/images/I/51VqN8YZPNL._SX679_.jpg"),
        
        # Foxtale
        Product(name="Daily Duet Sunscreen SPF 50", brand="Foxtale", price=699, category="Skincare",
                description="Broad spectrum sunscreen", stock=60,
                image_url="https://m.media-amazon.com/images/I/41xN8YZPNL._SX679_.jpg"),
        Product(name="Hydrating Face Wash", brand="Foxtale", price=449, category="Skincare",
                description="Gentle daily cleanser", stock=80,
                image_url="https://m.media-amazon.com/images/I/51xQqH7RKSL._SX679_.jpg"),
        
        # Minimalist
        Product(name="10% Niacinamide Face Serum", brand="Minimalist", price=599, category="Skincare",
                description="Pore minimizing serum", stock=70,
                image_url="https://m.media-amazon.com/images/I/41VqN8YZPNL._SX679_.jpg"),
        Product(name="2% Salicylic Acid Face Wash", brand="Minimalist", price=349, category="Skincare",
                description="Acne control cleanser", stock=85,
                image_url="https://m.media-amazon.com/images/I/51xN8YZPNL._SX679_.jpg"),
        
        # Plum
        Product(name="Green Tea Renewed Clarity Face Wash", brand="Plum", price=375, category="Skincare",
                description="Oil control face wash", stock=75,
                image_url="https://m.media-amazon.com/images/I/41xQqH7RKSL._SX679_.jpg"),
        Product(name="15% Vitamin C Face Serum", brand="Plum", price=795, category="Skincare",
                description="Brightening face serum", stock=55,
                image_url="https://m.media-amazon.com/images/I/51VqYqH8pPL._SX679_.jpg"),
        
        # Mamaearth
        Product(name="Vitamin C Face Wash", brand="Mamaearth", price=299, category="Skincare",
                description="Brightening face wash", stock=100,
                image_url="https://m.media-amazon.com/images/I/51VqN8YZPNL._SX679_.jpg"),
        Product(name="Onion Hair Oil", brand="Mamaearth", price=599, category="Haircare",
                description="Hair growth oil", stock=90,
                image_url="https://m.media-amazon.com/images/I/41xN8YZPNL._SX679_.jpg"),
        Product(name="Ubtan Face Wash", brand="Mamaearth", price=349, category="Skincare",
                description="Natural face cleanser", stock=85,
                image_url="https://m.media-amazon.com/images/I/51xQqH7RKSL._SX679_.jpg"),
        
        # WOW Skin Science
        Product(name="Apple Cider Vinegar Shampoo", brand="WOW Skin Science", price=499, category="Haircare",
                description="Hair strengthening shampoo", stock=70,
                image_url="https://m.media-amazon.com/images/I/41VqYqH8pPL._SX679_.jpg"),
        Product(name="Red Onion Hair Oil", brand="WOW Skin Science", price=599, category="Haircare",
                description="Hair fall control oil", stock=65,
                image_url="https://m.media-amazon.com/images/I/51VqN8YZPNL._SX679_.jpg"),
        
        # Biotique
        Product(name="Bio Kelp Protein Shampoo", brand="Biotique", price=299, category="Haircare",
                description="Falling hair shampoo", stock=80,
                image_url="https://m.media-amazon.com/images/I/41xN8YZPNL._SX679_.jpg"),
        Product(name="Bio Honey Gel Face Wash", brand="Biotique", price=225, category="Skincare",
                description="Refreshing foaming face wash", stock=90,
                image_url="https://m.media-amazon.com/images/I/51xQqH7RKSL._SX679_.jpg"),
    ]
    
    db.add_all(products)
    db.commit()
    print(f"✅ Added {len(products)} real market products!")
    
    # Show added products
    for p in products[:10]:
        print(f"  {p.brand} - {p.name} - ₹{p.price}")
    
    db.close()

if __name__ == "__main__":
    add_market_products()
