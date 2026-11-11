from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid

router = APIRouter(prefix="/api/payment", tags=["Payment"])

class OrderCreate(BaseModel):
    amount: float

class PaymentVerify(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str

@router.post("/create-order")
def create_order(order: OrderCreate):
    order_id = f"order_{uuid.uuid4().hex[:12]}"
    return {
        "order_id": order_id,
        "amount": int(order.amount * 100),
        "currency": "INR",
        "key": "rzp_test_demo"
    }

@router.post("/verify-payment")
def verify_payment(payment: PaymentVerify):
    return {"status": "success", "message": "Payment verified"}
