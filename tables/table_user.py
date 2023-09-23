# Models from sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer



Base = declarative_base()


# Table model: Users
class Table_users(Base):

    __tablename__ = "users"
    __table_args__ = {"schema" : "commercial"}

    id = Column(Integer, primary_key = True)
    name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    def __init__(self, id, name, last_name, age):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.age = age