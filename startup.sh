#!/bin/bash
# Launch FastAPI app via Gunicorn with UvicornWorker
# Entry point: server.py → app

gunicorn server:app \
  --workers 1 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --timeout 600 \
  --log-level debug