# Render Deployment - Exact Steps

## STEP 1: Deploy Backend First

1. Go to https://render.com/dashboard
2. Click **"New +"** → **"Web Service"**
3. Select repository: **beauty_store**
4. Fill in these EXACT values:

**Name:** `beauty-store-backend`

**Branch:** `main`

**Root Directory:** `backend`

**Runtime:** `Python 3`

**Build Command:** 
```
pip install -r requirements.txt
```

**Start Command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Environment Variables - Click "Add Environment Variable" for each:**

| Key | Value |
|-----|-------|
| `DATABASE_URL` | `sqlite:///./beauty.db` |
| `SECRET_KEY` | `your-secret-key-change-this-123456` |
| `RAZORPAY_KEY_ID` | `YOUR_RAZORPAY_LIVE_KEY` |
| `RAZORPAY_KEY_SECRET` | `YOUR_RAZORPAY_LIVE_SECRET` |

5. Click **"Create Web Service"**
6. Wait for deployment (2-3 minutes)
7. **COPY THE URL** (e.g., `https://beauty-store-backend.onrender.com`)

---

## STEP 2: Deploy Frontend

1. Go back to https://render.com/dashboard
2. Click **"New +"** → **"Static Site"**
3. Select repository: **beauty_store**
4. Fill in these EXACT values:

**Name:** `beauty-store`

**Branch:** `main`

**Root Directory:** `frontend`

**Build Command:**
```
npm install && npm run build
```

**Publish Directory:** `dist`

**Environment Variables - Click "Add Environment Variable" for each:**

| Key | Value |
|-----|-------|
| `VITE_API_URL` | Paste your backend URL from Step 1 |
| `VITE_RAZORPAY_KEY_ID` | `YOUR_RAZORPAY_LIVE_KEY` |

5. Click **"Deploy static site"**
6. Wait for deployment (3-5 minutes)
7. **YOUR WEBSITE IS LIVE!** Copy the URL

---

## STEP 3: Test on Mobile

1. Open the frontend URL on your mobile browser
2. Your website should work on any phone!

---

## Troubleshooting

If frontend can't connect to backend:
1. Go to Render Dashboard → beauty-store (frontend)
2. Click "Environment" 
3. Update `VITE_API_URL` with correct backend URL
4. Click "Save Changes" - it will redeploy automatically
