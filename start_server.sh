#!/bin/bash
pkill -9 uvicorn
sleep 2
cd /home/sagemaker-user/girlyy/backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
