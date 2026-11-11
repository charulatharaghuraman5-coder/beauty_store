from database import SessionLocal
from models import Product

db = SessionLocal()

products = db.query(Product).all()

for product in products:
    name_lower = product.name.lower()
    
    if "lipstick" in name_lower:
        product.image_url = "https://images.pexels.com/photos/2533266/pexels-photo-2533266.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "mascara" in name_lower:
        product.image_url = "https://images.pexels.com/photos/3373736/pexels-photo-3373736.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "foundation" in name_lower:
        product.image_url = "https://images.pexels.com/photos/3373714/pexels-photo-3373714.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "eyeshadow" in name_lower or "eye shadow" in name_lower or "palette" in name_lower:
        product.image_url = "https://images.pexels.com/photos/2533269/pexels-photo-2533269.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "blush" in name_lower:
        product.image_url = "https://images.pexels.com/photos/3373725/pexels-photo-3373725.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "perfume" in name_lower or "fragrance" in name_lower or "edt" in name_lower or "eau" in name_lower:
        product.image_url = "https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "shampoo" in name_lower:
        product.image_url = "https://images.pexels.com/photos/4465124/pexels-photo-4465124.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "conditioner" in name_lower:
        product.image_url = "https://images.pexels.com/photos/4465121/pexels-photo-4465121.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "serum" in name_lower and "hair" in name_lower:
        product.image_url = "https://images.pexels.com/photos/4465119/pexels-photo-4465119.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "serum" in name_lower:
        product.image_url = "https://images.pexels.com/photos/3762879/pexels-photo-3762879.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "moisturizer" in name_lower or "cream" in name_lower:
        product.image_url = "https://images.pexels.com/photos/3762882/pexels-photo-3762882.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "cleanser" in name_lower:
        product.image_url = "https://images.pexels.com/photos/4041392/pexels-photo-4041392.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "sunscreen" in name_lower:
        product.image_url = "https://images.pexels.com/photos/4041285/pexels-photo-4041285.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "nail" in name_lower or "polish" in name_lower:
        product.image_url = "https://images.pexels.com/photos/3373718/pexels-photo-3373718.jpeg?auto=compress&cs=tinysrgb&w=400"
    elif "lotion" in name_lower or "body" in name_lower:
        product.image_url = "https://images.pexels.com/photos/4465831/pexels-photo-4465831.jpeg?auto=compress&cs=tinysrgb&w=400"
    else:
        product.image_url = "https://images.pexels.com/photos/3373736/pexels-photo-3373736.jpeg?auto=compress&cs=tinysrgb&w=400"

db.commit()
print(f"Updated {len(products)} products with matching images")
db.close()
