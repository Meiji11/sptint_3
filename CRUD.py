from sqlalchemy.orm import sessionmaker
from main import engine
from config import SessionLocal
from models_db.oses import OS
from models_db.brands import Brand
from models_db.memory import Memory
from models_db.models import Model
from models_db.users import User
from datetime import date

Session = sessionmaker(bind=engine)
session = Session()

# # Добавляем os_name
# os_1 = OS(os_name = "IOS")
# os_2 = OS(os_name = "Android")
# os_3 = OS(os_name = "Windows")
# os_list = [os_2, os_3]
#
# session.add_all(os_list)
# session.add(os_1)
# session.commit()

# # Добавляем brands_name test
# session_insert_value = SessionLocal()
# brand_1 = Brand(brand_name = "Apple")
# brand_2 = Brand(brand_name = "Xiaomi")
# brand_3 = Brand(brand_name = "Samsung")
# brand_4 = Brand(brand_name = "Google")
# brand_5 = Brand(brand_name = "Nokia")
#
# session_insert_value.add(brand_5)
# session_insert_value.add_all([brand_1, brand_2, brand_3, brand_4])
# session_insert_value.commit()

# # Добавляем memory_size
# size_1 = Memory(memory_size = 32)
# size_2 = Memory(memory_size = 64)
# size_3 = Memory(memory_size = 128)
# size_4 = Memory(memory_size = 256)
# size_list = [size_1, size_2, size_3, size_4]
#
# session.add_all(size_list)
# # session.add(os_1)
# session.commit()

# # Добаляем models при помощи функции
# def create_models(session: Session, model_name: str, brand: int, os: int, memory_size: int, amount: int, price: float) -> Model:
#     new_model = Model(model_name=model_name, brand = brand, os = os, memory_size = memory_size, amount = amount, price = price)
#     session.add(new_model)
#     session.commit()
#     session.refresh(new_model)
#     return new_model
#
# new_model = create_models(session, model_name="Samsung Galaxy S24 FE 8", brand=4, os=1, memory_size=4, amount=7, price=64990)

# # Добаляем users при помощи функции
# def create_users(session: Session, user_name: str, user_mail: str, user_date_reg: date, user_orders: int) -> User:
#     new_user = User(user_name=user_name, user_mail=user_mail, user_date_reg=user_date_reg, user_orders=user_orders)
#     session.add(new_user)
#     session.commit()
#     session.refresh(new_user)
#     return new_user
#
# new_user = create_users(session, user_name="Boris Wats", user_mail="boris1233@mail.com", user_date_reg= "12.12.2024", user_orders=1)

# # # Функиця для добавления пользователя с несколькими заказами
# def create_user_with_orders(session: Session, user_name: str, user_mail: str, user_date_reg: date, orders: list[int]) -> User:
#     # Создаем нового пользователя
#     new_user = User(user_name=user_name, user_mail=user_mail, user_date_reg=user_date_reg)
#     session.add(new_user)
#     session.commit()  # Сохраняем нового пользователя в базе
#     # Добавляем заказы к пользователю
#     for order_id in orders:
#         order = session.get(Model, order_id) # Используем Session.get()
#         if order: # Если заказ существует
#             new_user.orders.append(order) # Связываем заказ с пользователем
#     session.commit() # Сохраняем все изменения
#     session.refresh(new_user) # Обновляем объект пользователя в сессии
#     return new_user
#
# # Создание сессии
# db: Session = SessionLocal()
#
# # Добавление нового пользователя с заказами
# new_user = create_user_with_orders(db, user_name="John Smith", user_mail="mark@mail.com", user_date_reg=date(2023, 3, 1), orders=[1, 2, 3])


user = session.query(User).filter_by(id=7).first()  # Найти пользователя по ID
if user:
    print(f"Заказы пользователя {user.user_name}:")
    for order in user.orders:
        print(f"- Order ID: {order.id}, Name: {order.model_name}, Price: {order.price}")
else:
    print("Пользователь не найден")