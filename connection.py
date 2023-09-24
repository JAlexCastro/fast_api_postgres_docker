# Info of database in Docker
Username = "fast_user"
Password = "fast_password"
Database_default = "company"
Host = "localhost"
Port = 9090

# Modules from Sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

URL = "postgresql://fast_user:fast_password@localhost:9090/company"

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



