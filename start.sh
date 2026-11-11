#!/bin/bash

echo "Starting Beauty Store Application..."
echo "====================================="

# Kill any existing processes
echo "Cleaning up existing processes..."
pkill -f "uvicorn main:app" 2>/dev/null || true
pkill -f "vite" 2>/dev/null || true
sleep 2

# Start backend on port 8001
echo "Starting backend on port 8001..."
cd /home/sagemaker-user/girlyy/backend
pip install -q -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001 --reload > backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend PID: $BACKEND_PID"

# Wait for backend to start
sleep 3

# Start frontend on port 8000
echo "Starting frontend on port 8000..."
cd /home/sagemaker-user/girlyy/frontend
npm install --silent 2>/dev/null
npm run dev > frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend PID: $FRONTEND_PID"

echo ""
echo "====================================="
echo "✓ Backend running at: http://localhost:8001"
echo "✓ Frontend running at: http://localhost:8000"
echo "====================================="
echo ""
echo "Open http://localhost:8000 in your browser"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Trap Ctrl+C to kill both processes
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT

wait
