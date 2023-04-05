from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


# driver://user:password@host:port/db_name
db_url = 'postgresql://user:1@127.0.0.1:5432/sqlalchemy_test'
engine = create_engine(db_url)
# подключение к базе данных

Base = declarative_base()
# базовый класс для таблиц

# создаем таблицу
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"({self.id} -> {self.title})"

Base.metadata.create_all(bind=engine)
# записываем таблицу базы данных

Sessionlocal = sessionmaker(bind=engine)
# создаем класс для сессий (один объект от данного класса - одна сессия)

session = Sessionlocal()
# создаем сессию

# new_product = Product(title='product1', price=120)
# создаем продукт (запись в таблицу)
# для orm создаем запрос на запись в таблицу

# session.add(new_product)
# добавляем запрос в сессию

# session.commit()
# отправляем набор запросов базу данных

# session.add(Product(title='product2', price=34))
# session.add(Product(title='product3', price=250))
# session.add(Product(title='product4', price=451))
# session.add(Product(title='product5', price=124))
# session.commit()

products = session.query(Product).all()
# получаем все записи из таблицы product
print(products)

res = session.query(Product).filter(Product.price > 100).all()
# получаем все записи из таблицы product у которых цена больше 100
print(res)

product3 = session.query(Product).get(3)
# получаем продукт под id 3
print(product3)

product4 = session.query(Product).get(4)
# session.delete(product4)
# удаляем продукт
# session.commit()
# сохраняем изменения в базу данных

product3.title = 'new title'
product3.price = 100
# изменяем продукт
session.commit()
# сохраняем\фиксируем изменения