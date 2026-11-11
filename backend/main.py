from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import models
from database import engine
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

if os.path.exists(frontend_dist):
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist, "assets")), name="assets")
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")

@app.get("/products-view")
async def products_view():
    products_file = os.path.join(os.path.dirname(__file__), "products.html")
    if os.path.exists(products_file):
        return FileResponse(products_file)
    return {"error": "not found"}

@app.get("/favicon.svg")
async def favicon():
    favicon_path = os.path.join(frontend_dist, "favicon.svg")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return {"error": "not found"}
