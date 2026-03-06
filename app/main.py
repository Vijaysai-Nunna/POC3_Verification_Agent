
from fastapi import FastAPI
from app.api.verify import router as verify_router
from app.database.db import engine
from app.database.models import Base

app = FastAPI(title="POC3 Verification Agent")

# Create tables automatically
Base.metadata.create_all(bind=engine)

app.include_router(verify_router)
