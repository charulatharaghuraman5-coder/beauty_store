from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import models
from database import engine, SessionLocal
from routers import users, products, cart, wishlist, orders, payment, auth
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Beauty E-Commerce API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_dist = os.path.join(os.path.dirname(__file__), "../frontend/dist")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(wishlist.router)
app.include_router(orders.router)
app.include_router(payment.router)
app.include_router(auth.router)

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/seed")
def seed_database():
    """Seed the database with sample products"""
    db = SessionLocal()
    try:
        existing = db.query(models.Product).count()
        if existing > 7:
            return {"message": f"Database already has {existing} products"}
        
        # Delete existing 7 products and add more
        db.query(models.Product).delete()
        db.commit()
        
        sample_products = [
            # Skincare (15 products)
            {"name": "Hydrating Face Serum", "description": "Intensive hydration serum", "price": 1299.00, "category": "Skincare", "brand": "GlowLab", "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400", "stock": 50},
            {"name": "Vitamin C Cream", "description": "Brightening day cream", "price": 899.00, "category": "Skincare", "brand": "RadiantSkin", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 75},
            {"name": "Gentle Cleanser", "description": "pH balanced cleanser", "price": 549.00, "category": "Skincare", "brand": "PureGlow", "image_url": "https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400", "stock": 100},
            {"name": "Night Repair Cream", "description": "Anti-aging night cream", "price": 1599.00, "category": "Skincare", "brand": "GlowLab", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 40},
            {"name": "Retinol Serum", "description": "Advanced retinol formula", "price": 1899.00, "category": "Skincare", "brand": "RadiantSkin", "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400", "stock": 35},
            {"name": "Sunscreen SPF 50", "description": "Broad spectrum protection", "price": 699.00, "category": "Skincare", "brand": "PureGlow", "image_url": "https://images.unsplash.com/photo-1532413992378-f169ac26fff0?w=400", "stock": 80},
            {"name": "Face Mask Set", "description": "5 sheet masks variety pack", "price": 499.00, "category": "Skincare", "brand": "GlowLab", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 90},
            {"name": "Eye Cream", "description": "Reduces dark circles", "price": 1199.00, "category": "Skincare", "brand": "RadiantSkin", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 55},
            {"name": "Toner", "description": "Balancing facial toner", "price": 649.00, "category": "Skincare", "brand": "PureGlow", "image_url": "https://images.unsplash.com/photo-1556228852-80c3b5e1c2c1?w=400", "stock": 70},
            {"name": "Exfoliating Scrub", "description": "Gentle face scrub", "price": 599.00, "category": "Skincare", "brand": "GlowLab", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 65},
            
            # Makeup (15 products)
            {"name": "Matte Lipstick", "description": "Long-lasting matte lipstick", "price": 699.00, "category": "Makeup", "brand": "ColorPop", "image_url": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400", "stock": 120},
            {"name": "HD Foundation", "description": "Full coverage foundation", "price": 1499.00, "category": "Makeup", "brand": "FlawlessBeauty", "image_url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400", "stock": 60},
            {"name": "Eyeshadow Palette", "description": "12 shade palette", "price": 1899.00, "category": "Makeup", "brand": "GlamEyes", "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400", "stock": 45},
            {"name": "Mascara", "description": "Volumizing mascara", "price": 799.00, "category": "Makeup", "brand": "ColorPop", "image_url": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=400", "stock": 85},
            {"name": "Blush Palette", "description": "3 shade blush palette", "price": 999.00, "category": "Makeup", "brand": "FlawlessBeauty", "image_url": "https://images.unsplash.com/photo-1596704017254-9b121068ec31?w=400", "stock": 70},
            {"name": "Eyeliner Pencil", "description": "Waterproof eyeliner", "price": 499.00, "category": "Makeup", "brand": "GlamEyes", "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400", "stock": 100},
            {"name": "Lip Gloss Set", "description": "5 glossy shades", "price": 899.00, "category": "Makeup", "brand": "ColorPop", "image_url": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400", "stock": 75},
            {"name": "Concealer", "description": "Full coverage concealer", "price": 799.00, "category": "Makeup", "brand": "FlawlessBeauty", "image_url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400", "stock": 80},
            {"name": "Setting Spray", "description": "Long-lasting makeup setter", "price": 699.00, "category": "Makeup", "brand": "GlamEyes", "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400", "stock": 90},
            {"name": "Bronzer", "description": "Sun-kissed glow", "price": 899.00, "category": "Makeup", "brand": "ColorPop", "image_url": "https://images.unsplash.com/photo-1596704017254-9b121068ec31?w=400", "stock": 65},
            
            # Haircare (10 products)
            {"name": "Argan Hair Serum", "description": "Nourishing hair serum", "price": 799.00, "category": "Haircare", "brand": "SilkHair", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400", "stock": 80},
            {"name": "Keratin Shampoo", "description": "Strengthening shampoo", "price": 649.00, "category": "Haircare", "brand": "HairRevive", "image_url": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400", "stock": 90},
            {"name": "Deep Conditioner", "description": "Intensive hair treatment", "price": 749.00, "category": "Haircare", "brand": "SilkHair", "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400", "stock": 70},
            {"name": "Hair Mask", "description": "Weekly repair treatment", "price": 899.00, "category": "Haircare", "brand": "HairRevive", "image_url": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400", "stock": 60},
            {"name": "Leave-in Spray", "description": "Detangling spray", "price": 599.00, "category": "Haircare", "brand": "SilkHair", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400", "stock": 85},
            
            # Fragrance (5 products)
            {"name": "Rose Perfume", "description": "Elegant floral fragrance", "price": 2499.00, "category": "Fragrance", "brand": "LuxeScent", "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "stock": 35},
            {"name": "Ocean Breeze EDT", "description": "Fresh aquatic scent", "price": 1799.00, "category": "Fragrance", "brand": "AquaEssence", "image_url": "https://images.unsplash.com/photo-1588405748880-12d1d2a59d75?w=400", "stock": 40},
            {"name": "Vanilla Musk", "description": "Warm vanilla fragrance", "price": 2199.00, "category": "Fragrance", "brand": "LuxeScent", "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "stock": 30},
            {"name": "Citrus Burst", "description": "Energizing citrus scent", "price": 1599.00, "category": "Fragrance", "brand": "AquaEssence", "image_url": "https://images.unsplash.com/photo-1588405748880-12d1d2a59d75?w=400", "stock": 45},
            {"name": "Night Jasmine", "description": "Exotic floral perfume", "price": 2699.00, "category": "Fragrance", "brand": "LuxeScent", "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "stock": 25},
            
            # Bath and Body (5 products)
            {"name": "Lavender Lotion", "description": "Moisturizing body lotion", "price": 599.00, "category": "Bath and Body", "brand": "BodyBliss", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 110},
            {"name": "Coconut Scrub", "description": "Exfoliating body scrub", "price": 749.00, "category": "Bath and Body", "brand": "TropicalGlow", "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400", "stock": 65},
            {"name": "Body Butter", "description": "Rich moisturizing butter", "price": 899.00, "category": "Bath and Body", "brand": "BodyBliss", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 55},
            {"name": "Bath Bombs Set", "description": "6 aromatherapy bath bombs", "price": 699.00, "category": "Bath and Body", "brand": "TropicalGlow", "image_url": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400", "stock": 75},
            {"name": "Shower Gel", "description": "Refreshing body wash", "price": 499.00, "category": "Bath and Body", "brand": "BodyBliss", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 95},
        ]
        
        for p in sample_products:
            db.add(models.Product(**p))
        db.commit()
        return {"message": f"Database seeded with {len(sample_products)} products!"}
    finally:
        db.close()

@app.get("/products-view")
async def products_view():
    products_file = os.path.join(os.path.dirname(__file__), "products.html")
    if os.path.exists(products_file):
        return FileResponse(products_file)
    return {"error": "not found"}

@app.get("/simple")
async def simple_products():
    simple_file = os.path.join(os.path.dirname(__file__), "simple_products.html")
    if os.path.exists(simple_file):
        return FileResponse(simple_file)
    return {"error": "not found"}

@app.get("/favicon.svg")
async def favicon():
    favicon_path = os.path.join(frontend_dist, "favicon.svg")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return {"error": "not found"}

if os.path.exists(frontend_dist):
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist, "assets")), name="assets")
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")
