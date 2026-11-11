# 🎯 QUICK START - Copy and Paste These Commands

## Step 1: Navigate to Backend Folder
```bash
cd /home/sagemaker-user/girlyy/backend
```

## Step 2: Install Required Packages
```bash
pip install -r requirements.txt
```

## Step 3: Create Database and Add Sample Products
```bash
python seed_data.py
```

## Step 4: Start the Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

OR use the startup script:
```bash
./start_server.sh
```

## Step 5: Open Swagger UI in Browser
```
http://localhost:8000/docs
```

---

## 🔥 What You Get

✅ **12 Sample Beauty Products** across 5 categories
✅ **Admin Account** - Username: `admin`, Password: `admin123`
✅ **Complete REST API** with all endpoints
✅ **Swagger UI** for testing
✅ **CORS Enabled** for React frontend

---

## 🔗 Connect React Frontend

In your React app, add this:

```javascript
// src/config.js or at the top of your component
const API_URL = "http://localhost:8000";

// Example: Fetch products
async function getProducts() {
  const response = await fetch(`${API_URL}/api/products/`);
  const data = await response.json();
  return data;
}

// Example: Register user
async function registerUser(userData) {
  const response = await fetch(`${API_URL}/api/users/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData)
  });
  return await response.json();
}

// Example: Login
async function loginUser(credentials) {
  const response = await fetch(`${API_URL}/api/users/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(credentials)
  });
  return await response.json();
}
```

---

## 📱 Test in Swagger UI

1. Go to http://localhost:8000/docs
2. Try these endpoints:
   - **GET /api/products/** - See all products
   - **POST /api/users/register** - Create account
   - **POST /api/users/login** - Login
   - **POST /api/cart/** - Add to cart

---

## 🛑 Stop the Server

Press `Ctrl + C` in the terminal

---

## 🔄 Reset Everything

```bash
rm beauty.db
python seed_data.py
```

---

## ✨ You're All Set!

Your backend is ready to use with your React frontend!
