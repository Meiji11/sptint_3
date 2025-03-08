#Декларатив Base. Отсюда буду импортировать его во все модели.
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Сохраняем ссылку на нашу БД
my_db_link_tele4 = ("postgresql+psycopg2://postgres:mdc77ak2@localhost/Tele-4")

#Создание движка
engine = create_engine(my_db_link_tele4)

# Создаем фабрику сессий
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()






# # Код для создания БД в PostgreSQL
# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#
# connection = psycopg2.connect(user="postgres", password="mdc77ak2", host = "localhost", port = "5432")
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#
# cursor=connection.cursor()
# sql_create_database = cursor.execute('CREATE DATABASE "Tele-4"')
#
# cursor.close()
# connection.close()