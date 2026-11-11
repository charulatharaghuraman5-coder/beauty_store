from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Product

db = SessionLocal()

products = db.query(Product).filter(Product.image_url.isnot(None), Product.image_url != "").all()

if len(products) > 300:
    to_delete = products[300:]
    for product in to_delete:
        db.delete(product)
    db.commit()
    print(f"Deleted {len(to_delete)} products. Kept 300 products with images.")
else:
    print(f"Only {len(products)} products with images found. No deletion needed.")

db.close()
