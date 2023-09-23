# Info of database
Username = "admin"
Password = "admin"
Database_default = "company"
Host = "localhost"
Port = 9090

# Modules from Sqlalchemt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

URL = "postgresql://admin:admin@localhost:9090/company"

engine = create_engine(URL)
Session = sessionmaker(bind=engine)
session = Session()


try:
    engine.connect()
    print("Successful connection Alchemy")
    session = Session()
    
except OperationalError as error:
    print("Connection Error")
    print(error)



