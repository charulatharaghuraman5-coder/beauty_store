# Beauty E-Commerce Backend API

Complete FastAPI backend for Nykaa-like Beauty E-Commerce Website

## 🚀 Quick Start Guide

### Step 1: Install Python Packages

Open terminal in the `backend` folder and run:

```bash
cd /home/sagemaker-user/girlyy/backend
pip install -r requirements.txt
```

### Step 2: Seed the Database with Sample Products

```bash
python seed_data.py
```

This will create:
- 12 sample beauty products across all categories
- Admin user (username: `admin`, password: `admin123`)

### Step 3: Start the FastAPI Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The server will start at: `http://localhost:8000`

### Step 4: Open Swagger UI (API Documentation)

Open your browser and go to:
```
http://localhost:8000/docs
```

You can test all API endpoints here!

---

## 📁 Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── database.py          # Database connection
├── models.py            # Database tables
├── schemas.py           # Data validation
├── seed_data.py         # Sample data
├── requirements.txt     # Python packages
├── beauty.db            # SQLite database (auto-created)
└── routers/
    ├── users.py         # User authentication
    ├── products.py      # Product management
    ├── cart.py          # Shopping cart
    ├── wishlist.py      # Wishlist
    └── orders.py        # Order management
```

---

## 🔌 API Endpoints

### Users (Authentication)
- `POST /api/users/register` - Create new account
- `POST /api/users/login` - Login
- `GET /api/users/me` - Get current user

### Products
- `GET /api/products/` - Get all products
- `GET /api/products/{id}` - Get product details
- `POST /api/products/` - Add product (Admin)
- `PUT /api/products/{id}` - Update product (Admin)
- `DELETE /api/products/{id}` - Delete product (Admin)
- `GET /api/products/categories/all` - Get all categories

### Shopping Cart
- `POST /api/cart/` - Add to cart
- `GET /api/cart/?user_id={id}` - Get cart items
- `PUT /api/cart/{id}` - Update quantity
- `DELETE /api/cart/{id}` - Remove from cart
- `GET /api/cart/total/{user_id}` - Get cart total

### Wishlist
- `POST /api/wishlist/` - Add to wishlist
- `GET /api/wishlist/?user_id={id}` - Get wishlist
- `DELETE /api/wishlist/{id}` - Remove from wishlist

### Orders
- `POST /api/orders/` - Place order
- `GET /api/orders/?user_id={id}` - Get user orders
- `GET /api/orders/{id}` - Get order details
- `PUT /api/orders/{id}/status` - Update order status (Admin)
- `GET /api/orders/admin/all` - Get all orders (Admin)

---

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication.

**Login Flow:**
1. Register: `POST /api/users/register`
2. Login: `POST /api/users/login` - Returns access token
3. Use token in subsequent requests

---

## 🛍️ Product Categories

1. **Skincare** - Face serums, creams, cleansers
2. **Makeup** - Lipsticks, foundations, eyeshadows
3. **Haircare** - Shampoos, serums, treatments
4. **Fragrance** - Perfumes, EDTs
5. **Bath and Body** - Lotions, scrubs, body care

---

## 🔗 Connect with React Frontend

In your React app, use this base URL:

```javascript
const API_BASE_URL = "http://localhost:8000";

// Example: Fetch all products
fetch(`${API_BASE_URL}/api/products/`)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## 🧪 Testing with Swagger UI

1. Go to `http://localhost:8000/docs`
2. Click on any endpoint
3. Click "Try it out"
4. Fill in parameters
5. Click "Execute"
6. See the response!

---

## 👤 Default Admin Account

- **Username:** admin
- **Password:** admin123
- **Email:** admin@beauty.com

---

## 🛠️ Common Commands

**Start server:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Stop server:**
Press `Ctrl + C` in terminal

**Reset database:**
```bash
rm beauty.db
python seed_data.py
```

---

## 📝 Sample API Requests

### Register User
```json
POST /api/users/register
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "password123",
  "full_name": "John Doe"
}
```

### Login
```json
POST /api/users/login
{
  "username": "johndoe",
  "password": "password123"
}
```

### Add Product (Admin)
```json
POST /api/products/
{
  "name": "New Product",
  "description": "Product description",
  "price": 999.00,
  "category": "Skincare",
  "brand": "BrandName",
  "image_url": "https://example.com/image.jpg",
  "stock": 50
}
```

### Add to Cart
```json
POST /api/cart/?user_id=1
{
  "product_id": 1,
  "quantity": 2
}
```

### Place Order
```json
POST /api/orders/?user_id=1
{
  "shipping_address": "123 Main St, City, Country",
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    }
  ]
}
```

---

## ✅ Features Implemented

✓ User registration and login with password hashing
✓ JWT authentication
✓ Product CRUD operations
✓ Product search and filtering by category
✓ Shopping cart with quantity management
✓ Wishlist functionality
✓ Order placement and tracking
✓ Order history
✓ Admin product management
✓ Admin order management
✓ CORS enabled for React frontend
✓ SQLite database
✓ Swagger UI documentation
✓ Sample beauty products

---

## 🎯 Next Steps

1. Install packages: `pip install -r requirements.txt`
2. Seed database: `python seed_data.py`
3. Start server: `uvicorn main:app --reload --host 0.0.0.0 --port 8000`
4. Test APIs: `http://localhost:8000/docs`
5. Connect React frontend to `http://localhost:8000`

---

## 🐛 Troubleshooting

**Port already in use:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

**Module not found:**
```bash
pip install -r requirements.txt
```

**Database locked:**
```bash
rm beauty.db
python seed_data.py
```

---

## 📞 Support

Your FastAPI backend is ready! Test it with Swagger UI and connect it to your React frontend.

Happy Coding! 🚀
