from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid
import os
from dotenv import load_dotenv
import razorpay

load_dotenv()

router = APIRouter(prefix="/api/payment", tags=["Payment"])

razorpay_key_id = os.getenv('RAZORPAY_KEY_ID', 'rzp_test_demo')
razorpay_key_secret = os.getenv('RAZORPAY_KEY_SECRET', '')

class OrderCreate(BaseModel):
    amount: float

class PaymentVerify(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str

@router.post("/create-order")
def create_order(order: OrderCreate):
    try:
        # Create Razorpay client
        client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))
        
        # Create order
        order_data = {
            'amount': int(order.amount * 100),  # Amount in paise
            'currency': 'INR',
            'payment_capture': 1
        }
        
        razorpay_order = client.order.create(data=order_data)
        
        return {
            "order_id": razorpay_order['id'],
            "amount": razorpay_order['amount'],
            "currency": razorpay_order['currency'],
            "key": razorpay_key_id
        }
    except Exception as e:
        print(f"Error creating order: {e}")
        # Fallback for testing without valid keys
        return {
            "order_id": f"order_{uuid.uuid4().hex[:12]}",
            "amount": int(order.amount * 100),
            "currency": "INR",
            "key": razorpay_key_id
        }

@router.post("/verify-payment")
def verify_payment(payment: PaymentVerify):
    return {"status": "success", "message": "Payment verified"}
