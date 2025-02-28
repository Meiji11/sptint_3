from sqlalchemy import Table, Column, Integer, ForeignKey
from config import Base

user_orders_association =Table(
    'user_orders',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('order_id', Integer, ForeignKey('models.id'))
)
