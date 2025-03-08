from sqlalchemy import Column, String, Integer, ForeignKey, Float
from config import Base

class Memory(Base):
    __tablename__ = "memory"
    id = Column (Integer, primary_key=True)
    memory_size = Column (Integer, nullable=False)
