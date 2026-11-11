from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random
import requests

router = APIRouter(prefix="/api/auth", tags=["Auth"])

# MSG91 API (100 free SMS - Get from https://msg91.com/)
MSG91_AUTH_KEY = "588706AexkITnZC6af2b6f3P1"

# Store OTPs temporarily
otp_store = {}

class SendOTPRequest(BaseModel):
    phone_number: str

class VerifyOTPRequest(BaseModel):
    phone_number: str
    otp: str

@router.post("/send-otp")
def send_otp(request: SendOTPRequest):
    try:
        # Generate 6 digit OTP
        otp = str(random.randint(100000, 999999))
        
        # Store OTP
        otp_store[request.phone_number] = otp
        
        # Send SMS via MSG91 (Free 100 SMS)
        url = f"https://control.msg91.com/api/v5/otp?mobile=91{request.phone_number}&otp={otp}"
        headers = {
            "authkey": MSG91_AUTH_KEY,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return {"status": "success", "message": f"OTP sent to +91{request.phone_number}"}
            else:
                # Fallback
                return {"status": "success", "message": "OTP sent", "otp": otp, "note": "SMS service not configured. Use this OTP."}
        except:
            # Fallback
            return {"status": "success", "message": "OTP sent", "otp": otp, "note": "Use this OTP to login."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/verify-otp")
def verify_otp(request: VerifyOTPRequest):
    stored_otp = otp_store.get(request.phone_number)
    
    if not stored_otp:
        raise HTTPException(status_code=400, detail="OTP expired or not found")
    
    if stored_otp == request.otp:
        del otp_store[request.phone_number]
        return {"status": "success", "message": "OTP verified"}
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP")
