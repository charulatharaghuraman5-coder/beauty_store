from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas
from database import get_db

router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("/categories/all")
def get_categories():
    return {
        "categories": [
            "Skincare",
            "Makeup",
            "Haircare",
            "Fragrance",
            "Bath and Body"
        ]
    }

@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=List[schemas.ProductResponse])
def get_all_products(
    response: Response,
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    response.headers["Access-Control-Expose-Headers"] = "*"
    response.headers["Cache-Control"] = "no-cache"
    
    query = db.query(models.Product)
    
    if category:
        query = query.filter(models.Product.category == category)
    
    if search:
        query = query.filter(models.Product.name.contains(search))
    
    products = query.offset(skip).limit(limit).all()
    return products

@router.get("/exact/{product_name}", response_model=schemas.ProductResponse)
def get_product_by_exact_name(product_name: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/image/{product_name}")
def get_product_image_by_name(product_name: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.name == product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"image_url": product.image_url}

@router.post("/update-images")
def update_product_images(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    updated = 0
    
    for product in products:
        name_lower = product.name.lower()
        
        if "lipstick" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"
        elif "mascara" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400"
        elif "foundation" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400"
        elif "eyeshadow" in name_lower or "eye shadow" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"
        elif "blush" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1596704017254-9b121068ec31?w=400"
        elif "perfume" in name_lower or "fragrance" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400"
        elif "shampoo" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400"
        elif "conditioner" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400"
        elif "serum" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400"
        elif "moisturizer" in name_lower or "cream" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400"
        elif "cleanser" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"
        elif "sunscreen" in name_lower:
            product.image_url = "https://images.unsplash.com/photo-1532413992378-f169ac26fff0?w=400"
        else:
            continue
        
        updated += 1
    
    db.commit()
    return {"message": f"Updated {updated} product images"}

@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product_update: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product_update.dict(exclude_unset=True).items():
        setattr(product, key, value)
    
    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
