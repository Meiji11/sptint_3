from sqlalchemy import Column, String, Integer, ForeignKey, Float
from config import Base
from sqlalchemy.orm import relationship

class Model(Base):
    __tablename__ = "models"
    id = Column (Integer, primary_key=True)
    model_name = Column (String(30), nullable=False)
    brand_relat = relationship("Brand", backref="models")
    brand = Column (Integer, ForeignKey('brands.id'))
    os_relat = relationship("OS", backref="models")
    os = Column (Integer, ForeignKey('oses.id'))
    memory = relationship("Memory", backref="models")
    memory_size = Column (Integer, ForeignKey('memory.id'))
    amount = Column (Integer)
    price = Column (Float)




