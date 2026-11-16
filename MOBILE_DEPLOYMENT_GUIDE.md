# STEP-BY-STEP: Make Your Website Visible on Mobile

## STEP 1: Get GitHub Personal Access Token

1. Open browser, go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name it: "beauty_store"
4. Check the box: ☑ repo (full control of private repositories)
5. Scroll down, click "Generate token"
6. COPY THE TOKEN (starts with ghp_) - you'll need it next!

---

## STEP 2: Push Code to GitHub

Open terminal and run these commands ONE BY ONE:

```bash
cd /home/sagemaker-user/girlyy
```

```bash
git add .
```

```bash
git commit -m "Ready for deployment"
```

```bash
git remote set-url origin https://YOUR_TOKEN_HERE@github.com/charulatharaghuraman5-coder/beauty_store.git
```
(Replace YOUR_TOKEN_HERE with the token you copied)

```bash
git push origin main
```

---

## STEP 3: Deploy Backend on Render

1. Open browser, go to: https://render.com
2. Click "Get Started" or "Sign In"
3. Click "Sign in with GitHub"
4. Authorize Render
5. Click "New +" button (top right)
6. Select "Web Service"
7. Find and click "beauty_store" repository
8. Click "Connect"

**Fill in these fields:**

Name:
```
beauty-store-backend
```

Branch:
```
main
```

Root Directory:
```
backend
```

Runtime:
```
Python 3
```

Build Command:
```
pip install -r requirements.txt
```

Start Command:
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Add Environment Variables (click "Add Environment Variable" 4 times):**

Variable 1:
- Key: `DATABASE_URL`
- Value: `sqlite:///./beauty.db`

Variable 2:
- Key: `SECRET_KEY`
- Value: `my-secret-key-12345`

Variable 3:
- Key: `RAZORPAY_KEY_ID`
- Value: [YOUR RAZORPAY LIVE KEY]

Variable 4:
- Key: `RAZORPAY_KEY_SECRET`
- Value: [YOUR RAZORPAY LIVE SECRET]

9. Click "Create Web Service" (bottom of page)
10. WAIT 2-3 minutes for deployment
11. **COPY THE URL** at the top (looks like: https://beauty-store-backend.onrender.com)
12. SAVE THIS URL - you need it for the next step!

---

## STEP 4: Deploy Frontend on Render

1. Go back to: https://render.com/dashboard
2. Click "New +" button (top right)
3. Select "Static Site"
4. Find and click "beauty_store" repository
5. Click "Connect"

**Fill in these fields:**

Name:
```
beauty-store
```

Branch:
```
main
```

Root Directory:
```
frontend
```

Build Command:
```
npm install && npm run build
```

Publish Directory:
```
dist
```

**Add Environment Variables (click "Add Environment Variable" 2 times):**

Variable 1:
- Key: `VITE_API_URL`
- Value: [PASTE YOUR BACKEND URL FROM STEP 3]

Variable 2:
- Key: `VITE_RAZORPAY_KEY_ID`
- Value: [YOUR RAZORPAY LIVE KEY]

6. Click "Create Static Site" (bottom of page)
7. WAIT 3-5 minutes for deployment
8. **YOUR WEBSITE IS LIVE!** Copy the URL at the top

---

## STEP 5: Open on Mobile Phone

1. Copy the frontend URL (looks like: https://beauty-store.onrender.com)
2. Open this URL on ANY mobile phone browser
3. Your website works on mobile! 🎉

---

## Troubleshooting

**If frontend can't connect to backend:**
1. Go to Render Dashboard
2. Click on "beauty-store" (frontend)
3. Click "Environment" tab
4. Update `VITE_API_URL` with correct backend URL
5. Click "Save Changes"
6. Wait for automatic redeploy

**If you see errors:**
- Check that all environment variables are correct
- Make sure Razorpay keys are LIVE keys (start with rzp_live_)
- Wait a few minutes - first deployment can be slow

---

## Your Website URLs

Backend API: https://beauty-store-backend.onrender.com
Frontend (Main Website): https://beauty-store.onrender.com

Share the frontend URL with anyone to access your website!
