#!/bin/bash

echo "🌸 Starting Beauty Store on Port 8000..."

# Kill all existing servers
pkill -9 -f "uvicorn" 2>/dev/null
pkill -9 -f "vite" 2>/dev/null
pkill -9 -f "http.server" 2>/dev/null
sleep 2

# Build frontend
cd /home/sagemaker-user/girlyy/frontend
npm run build

# Start unified server on port 8000
cd /home/sagemaker-user/girlyy/backend
rm -rf __pycache__
python -m uvicorn main:app --host 0.0.0.0 --port 8000 &

sleep 5

echo ""
echo "✅ Beauty Store running on http://localhost:8000"
echo "✅ API endpoints available at http://localhost:8000/api/*"
echo "✅ API docs at http://localhost:8000/docs"
echo ""
