from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product

def update_product_images():
    db = SessionLocal()
    
    # Update all products with accessible image URLs
    products = db.query(Product).all()
    
    for product in products:
        category = product.category.lower()
        
        if category == "skincare":
            if "serum" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400"
            elif "face wash" in product.name.lower() or "cleanser" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"
            elif "moisturizer" in product.name.lower() or "cream" in product.name.lower() or "gel" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400"
            elif "sunscreen" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1532413992378-f169ac26fff0?w=400"
            else:
                product.image_url = "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400"
        
        elif category == "makeup":
            if "lipstick" in product.name.lower() or "lip" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"
            elif "foundation" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400"
            elif "kajal" in product.name.lower() or "mascara" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400"
            else:
                product.image_url = "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"
        
        elif category == "haircare":
            if "shampoo" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400"
            elif "oil" in product.name.lower():
                product.image_url = "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400"
            else:
                product.image_url = "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400"
        
        elif category == "bodycare":
            product.image_url = "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"
        
        else:
            product.image_url = "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400"
    
    db.commit()
    print(f"✅ Updated images for {len(products)} products!")
    
    # Show first 5
    for p in products[:5]:
        print(f"  {p.brand} - {p.name}")
        print(f"    Image: {p.image_url}")
    
    db.close()

if __name__ == "__main__":
    update_product_images()
