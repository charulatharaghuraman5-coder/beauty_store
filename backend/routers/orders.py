from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(prefix="/api/orders", tags=["Orders"])

@router.post("/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, user_id: int, db: Session = Depends(get_db)):
    total_amount = 0
    order_items_data = []
    
    for item in order.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        
        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for {product.name}")
        
        item_total = product.price * item.quantity
        total_amount += item_total
        order_items_data.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "price": product.price
        })
    
    new_order = models.Order(
        user_id=user_id,
        total_amount=total_amount,
        shipping_address=order.shipping_address,
        shipping_fullname=order.shipping_fullname,
        shipping_mobile=order.shipping_mobile,
        shipping_city=order.shipping_city,
        shipping_pincode=order.shipping_pincode,
        shipping_state=order.shipping_state,
        payment_method=order.payment_method,
        payment_id=order.payment_id,
        status="Pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    for item_data in order_items_data:
        order_item = models.OrderItem(
            order_id=new_order.id,
            **item_data
        )
        db.add(order_item)
        
        product = db.query(models.Product).filter(models.Product.id == item_data["product_id"]).first()
        product.stock -= item_data["quantity"]
    
    db.query(models.CartItem).filter(models.CartItem.user_id == user_id).delete()
    
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/", response_model=List[schemas.OrderResponse])
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    orders = db.query(models.Order).filter(models.Order.user_id == user_id).order_by(models.Order.created_at.desc()).all()
    return orders

@router.get("/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}/status")
def update_order_status(order_id: int, status: str, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    valid_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    order.status = status
    db.commit()
    return {"message": "Order status updated successfully"}

@router.get("/admin/all", response_model=List[schemas.OrderResponse])
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(models.Order).order_by(models.Order.created_at.desc()).all()
    return orders
