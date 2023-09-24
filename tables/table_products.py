# Models from sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float



Base = declarative_base()


# Table model: products
class Table_products(Base):

    __tablename__ = "products"
    __table_args__ = {"schema" : "store"}

    code = Column(String, primary_key = True)
    product_name = Column(String)
    stock = Column(Integer)
    price = Column(Float)

    def __init__(self, code, product_name, stock, price):
        self.code = code
        self.product_name = product_name
        self.stock = stock
        self.price = price


