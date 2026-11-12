from fastapi import FastAPI
from routers import products

app = FastAPI()

try:
    app.include_router(products.router)
    print(f"✓ Products router included with {len(products.router.routes)} routes")
    print("Routes:")
    for route in app.routes:
        if hasattr(route, 'path'):
            print(f"  {route.path}")
except Exception as e:
    print(f"✗ Error including router: {e}")
    import traceback
    traceback.print_exc()
