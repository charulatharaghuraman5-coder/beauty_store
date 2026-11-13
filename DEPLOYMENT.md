# Deploy to Render

## Steps:

### 1. Push to GitHub
```bash
git add .
git commit -m "Add deployment config"
git push origin development
```

### 2. Deploy Backend on Render

1. Go to https://render.com and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: girlyy-backend
   - **Root Directory**: backend
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add Environment Variables:
   - `RAZORPAY_KEY_ID` = your_live_key
   - `RAZORPAY_KEY_SECRET` = your_live_secret
   - `SECRET_KEY` = any_random_string
   - `DATABASE_URL` = sqlite:///./beauty.db
6. Click "Create Web Service"
7. Copy the backend URL (e.g., https://girlyy-backend.onrender.com)

### 3. Deploy Frontend on Render

1. Click "New +" → "Static Site"
2. Connect same GitHub repository
3. Configure:
   - **Name**: girlyy-frontend
   - **Root Directory**: frontend
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: dist
4. Add Environment Variable:
   - `VITE_API_URL` = your_backend_url_from_step_2
   - `VITE_RAZORPAY_KEY_ID` = your_live_key
5. Click "Create Static Site"

### 4. Access Your Website
Your frontend URL will be: https://girlyy-frontend.onrender.com

**Note**: Free tier may take 1-2 minutes to wake up after inactivity.

## Alternative: Deploy Both Together

You can also use the render.yaml file:
1. Go to Render Dashboard
2. Click "New +" → "Blueprint"
3. Connect your repository
4. Render will auto-detect render.yaml and deploy both services
