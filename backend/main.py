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
        if existing > 0:
            return {"message": f"Database already has {existing} products"}
        
        sample_products = [
            {"name": "Hydrating Face Serum", "price": 1299.00, "category": "Skincare", "brand": "GlowLab", "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400", "stock": 50},
            {"name": "Vitamin C Cream", "price": 899.00, "category": "Skincare", "brand": "RadiantSkin", "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400", "stock": 75},
            {"name": "Matte Lipstick", "price": 699.00, "category": "Makeup", "brand": "ColorPop", "image_url": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400", "stock": 120},
            {"name": "HD Foundation", "price": 1499.00, "category": "Makeup", "brand": "FlawlessBeauty", "image_url": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400", "stock": 60},
            {"name": "Argan Hair Serum", "price": 799.00, "category": "Haircare", "brand": "SilkHair", "image_url": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400", "stock": 80},
            {"name": "Rose Perfume", "price": 2499.00, "category": "Fragrance", "brand": "LuxeScent", "image_url": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400", "stock": 35},
            {"name": "Lavender Lotion", "price": 599.00, "category": "Bath and Body", "brand": "BodyBliss", "image_url": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=400", "stock": 110},
        ]
        
        for p in sample_products:
            db.add(models.Product(**p))
        db.commit()
        return {"message": "Database seeded with products!"}
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
