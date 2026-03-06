
from app.database.db import SessionLocal
from app.database.models import Verification

def save_verification(data):
    db = SessionLocal()

    record = Verification(
        full_name=data["full_name"],
        date_of_birth=data["date_of_birth"],
        gender=data["gender"],
        document_number=data["document_number"]
    )

    db.add(record)
    db.commit()
    db.close()
