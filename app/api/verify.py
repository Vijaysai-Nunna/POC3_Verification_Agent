
from fastapi import APIRouter
from app.agents.ocr_agent import ocr_extract
from app.database.repository import save_verification

router = APIRouter()

@router.post("/verify")
def verify_document(data: dict):
    extracted = ocr_extract(data)
    save_verification(extracted)

    return {
        "message": "OCR extraction completed and stored in database",
        "extracted_data": extracted
    }
