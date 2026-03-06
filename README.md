
POC3 Verification Agent (Day 1–4)

Features:
- FastAPI backend
- OCR extraction agent (simulated)
- PostgreSQL storage
- Verification API

Setup:

py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Update PostgreSQL password in:
app/database/db.py

Run:
py run.py

Open:
http://127.0.0.1:8000/docs
