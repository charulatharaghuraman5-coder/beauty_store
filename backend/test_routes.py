from fastapi import FastAPI
from routers import products

app = FastAPI()
app.include_router(products.router)

print("Routes registered:")
for route in app.routes:
    if hasattr(route, 'path'):
        print(f"  {route.path}")
