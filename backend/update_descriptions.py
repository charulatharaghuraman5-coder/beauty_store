from sqlalchemy.orm import Session
from database import SessionLocal
import models

db = SessionLocal()

# Update descriptions for existing products
products = db.query(models.Product).all()

descriptions = {
    "Vitamin C + E Super Bright Serum": "Powerful brightening serum with 10% Vitamin C and Vitamin E to reduce dark spots and improve skin radiance",
    "Watermelon Hyaluronic Cooling Gel": "Lightweight gel moisturizer with watermelon and hyaluronic acid for 72-hour hydration and cooling effect",
    "9 to 5 Primer Matte Lipstick": "Long-lasting matte lipstick with primer for smooth application and all-day wear",
    "Absolute Skin Natural Mousse": "Lightweight mousse foundation for natural coverage and flawless finish",
    "Eyeconic Kajal": "Smudge-proof, waterproof black kajal for intense eye definition",
    "Revitalift Crystal Micro-Essence": "Anti-aging face essence with micro-crystals to reduce wrinkles and improve skin texture",
    "Infallible Pro-Matte Foundation": "24-hour matte finish foundation with full coverage and oil control",
    "Color Riche Matte Lipstick": "Rich, creamy matte lipstick with intense color payoff",
    "Fit Me Matte Foundation": "Natural matte foundation that matches your skin tone perfectly",
    "SuperStay Matte Ink Lipstick": "16-hour liquid matte lipstick that stays put without drying",
    "Colossal Kajal": "Intense black kajal with smudge-proof formula for bold eye looks",
    "Soft Light Moisturizer SPF 30": "Daily moisturizer with SPF 30 protection for soft, protected skin",
    "Lip Balm Cherry Shine": "Moisturizing lip balm with cherry flavor and natural shine",
    "Body Lotion Nourishing": "48-hour deep moisture body lotion for soft, smooth skin",
    "Daily Duet Sunscreen SPF 50": "Broad spectrum SPF 50 sunscreen for daily sun protection",
    "Hydrating Face Wash": "Gentle daily cleanser that hydrates while removing impurities",
    "10% Niacinamide Face Serum": "Pore minimizing serum with 10% niacinamide to reduce blemishes",
    "2% Salicylic Acid Face Wash": "Acne control cleanser with salicylic acid to fight breakouts",
    "Green Tea Renewed Clarity Face Wash": "Oil control face wash with green tea for clear, fresh skin",
    "15% Vitamin C Face Serum": "Brightening face serum with 15% vitamin C for glowing skin",
    "Vitamin C Face Wash": "Brightening face wash with vitamin C to improve skin tone",
    "Onion Hair Oil": "Hair growth oil with onion extract to reduce hair fall and promote growth",
    "Ubtan Face Wash": "Natural face cleanser with turmeric and sandalwood for glowing skin",
    "Apple Cider Vinegar Shampoo": "Hair strengthening shampoo with apple cider vinegar for healthy hair",
    "Red Onion Hair Oil": "Hair fall control oil with red onion extract and natural oils",
    "Bio Kelp Protein Shampoo": "Falling hair shampoo with kelp protein to strengthen hair",
    "Bio Honey Gel Face Wash": "Refreshing foaming face wash with honey for clean, soft skin",
    "Yardley London Gentleman Eau de Parfum": "Classic masculine fragrance with woody and spicy notes",
    "Engage W1 Perfume Spray": "Long-lasting perfume for women with floral and fruity notes",
    "Wild Stone Code Titanium Perfume": "Bold and intense fragrance with masculine appeal",
    "Bella Vita Luxury CEO Man Perfume": "Premium luxury perfume with sophisticated scent",
    "Skinn by Titan Celeste Eau de Parfum": "Elegant floral fragrance for confident women",
    "Park Avenue Storm Deodorant": "Fresh deodorant spray with long-lasting protection",
    "Fogg Scent Xpressio Fragrance": "Long-lasting body spray with captivating scent",
    "Denver Hamilton Deodorant": "Classic masculine deodorant with fresh fragrance",
    "Dove Deeply Nourishing Body Wash": "Moisturizing body wash with ¼ moisturizing cream",
    "The Body Shop Vitamin E Body Butter": "Intense moisture body butter with vitamin E for dry skin",
    "Vaseline Intensive Care Body Lotion": "Deep restore body lotion for extremely dry skin",
    "Himalaya Nourishing Body Lotion": "Natural body moisturizer with aloe vera and winter cherry",
    "Neutrogena Deep Moisture Body Lotion": "24-hour hydration lotion with glycerin",
    "Palmolive Naturals Shower Gel": "Refreshing shower gel with natural extracts",
    "Fiama Di Wills Gel Bar": "Skin conditioning gel bar with natural ingredients",
    "Lux Velvet Touch Body Wash": "Luxurious body wash with French rose and almond oil",
    "Pears Pure & Gentle Body Wash": "Gentle cleansing body wash with glycerin",
    "Biotique Bio Honey Gel Body Wash": "Natural honey body wash for soft, glowing skin",
}

updated = 0
for product in products:
    if product.name in descriptions:
        product.description = descriptions[product.name]
        updated += 1

db.commit()
print(f"✅ Updated descriptions for {updated} products")
db.close()
