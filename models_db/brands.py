from sqlalchemy import Column, String, Integer, ForeignKey, Float
from config import Base

class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key = True)
    brand_name = Column(String(30), nullable=False)