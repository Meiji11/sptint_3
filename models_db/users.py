from config import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date,Table
from sqlalchemy.orm import relationship

user_orders_association =Table(
    'user_orders',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('order_id', Integer, ForeignKey('models.id'))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    user_name = Column (String(30), nullable=False)
    user_mail = Column (String(40), nullable=False)
    user_date_reg = Column (Date)
    orders = relationship("Model", secondary=user_orders_association, backref="users")

