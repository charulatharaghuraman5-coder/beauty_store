# 🌸 Beauty Store - Server Status

## ✅ Both Servers Running Successfully!

### Backend API (Port 8001)
- **URL**: http://localhost:8001
- **Status**: ✅ Running
- **API Docs**: http://localhost:8001/docs
- **Health Check**: http://localhost:8001/health

### Frontend (Port 8000)
- **URL**: http://localhost:8000
- **Status**: ✅ Running
- **Framework**: React + Vite

## 🔧 Configuration Fixed

1. **Backend** runs on port **8001**
2. **Frontend** runs on port **8000** with proxy to backend
3. **Allowed hosts** configured for SageMaker Studio
4. **CORS** enabled for cross-origin requests

## 🌐 Access Your Application

Open in browser: **http://localhost:8000**

Or use the OPEN_HERE.html file in the project root.

## 📝 Server Management

### Check Running Processes
```bash
ps aux | grep -E "(uvicorn|vite)" | grep -v grep
```

### Stop Servers
```bash
ps aux | grep uvicorn | grep -v grep | awk '{print $2}' | xargs kill -9
ps aux | grep vite | grep -v grep | awk '{print $2}' | xargs kill -9
```

### Restart Servers
```bash
# Backend
cd /home/sagemaker-user/girlyy/backend
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload &

# Frontend
cd /home/sagemaker-user/girlyy/frontend
npm run dev &
```
