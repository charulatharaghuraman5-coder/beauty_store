from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(prefix="/api/wishlist", tags=["Wishlist"])

@router.post("/", response_model=schemas.WishlistItemResponse)
def add_to_wishlist(wishlist_item: schemas.WishlistItemCreate, user_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == wishlist_item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    existing_item = db.query(models.WishlistItem).filter(
        models.WishlistItem.user_id == user_id,
        models.WishlistItem.product_id == wishlist_item.product_id
    ).first()
    
    if existing_item:
        raise HTTPException(status_code=400, detail="Product already in wishlist")
    
    new_wishlist_item = models.WishlistItem(
        user_id=user_id,
        product_id=wishlist_item.product_id
    )
    db.add(new_wishlist_item)
    db.commit()
    db.refresh(new_wishlist_item)
    return new_wishlist_item

@router.get("/", response_model=List[schemas.WishlistItemResponse])
def get_wishlist(user_id: int, db: Session = Depends(get_db)):
    wishlist_items = db.query(models.WishlistItem).filter(models.WishlistItem.user_id == user_id).all()
    return wishlist_items

@router.delete("/{wishlist_item_id}")
def remove_from_wishlist(wishlist_item_id: int, db: Session = Depends(get_db)):
    wishlist_item = db.query(models.WishlistItem).filter(models.WishlistItem.id == wishlist_item_id).first()
    if not wishlist_item:
        raise HTTPException(status_code=404, detail="Wishlist item not found")
    
    db.delete(wishlist_item)
    db.commit()
    return {"message": "Item removed from wishlist"}
