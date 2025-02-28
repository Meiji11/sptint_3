from config import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from association_table import user_orders_association

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    user_name = Column (String(30), nullable=False)
    user_mail = Column (String(40), nullable=False)
    user_date_reg = Column (Date)
    order = relationship("Model", secondary=user_orders_association, backref="users")
    user_orders = Column (Integer, ForeignKey('models.id'))
