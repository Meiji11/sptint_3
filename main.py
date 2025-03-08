from config import Base, SessionLocal, engine, Session
from models_db.brands import Brand
from models_db.oses import OS
from models_db.memory import Memory
from models_db.users import User
from models_db.models import Model


# Создаем таблицы
Base.metadata.create_all(bind=engine)



