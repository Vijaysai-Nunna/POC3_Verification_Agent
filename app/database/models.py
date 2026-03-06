
from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Verification(Base):
    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    date_of_birth = Column(String)
    gender = Column(String)
    document_number = Column(String)
