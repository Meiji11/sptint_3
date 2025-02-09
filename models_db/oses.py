from sqlalchemy import Column, String, Integer
from config import Base

class OS(Base):
    __tablename__ = "oses"
    id = Column (Integer, primary_key=True)
    os_name = Column (String(30), nullable=False)
