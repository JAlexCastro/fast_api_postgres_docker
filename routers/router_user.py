import sys
import os

# Get the root directory path of your project
ruta_proyecto = os.path.dirname(os.path.dirname(__file__))

# Add the path to sys.path (To the root directory)
sys.path.append(ruta_proyecto)


# Models from FastAPI
from fastapi import APIRouter, HTTPException

# Internals Models
from schemas.schemas_user import UserCreate, UserUpdate
from tables.table_user import Table_users
from connection import session


router_user = APIRouter()

# Get User by ID
@router_user.get("/user{user_id}", summary="Get User by ID", description="Get information from an existing User")
def get_user(id:int):

    user = session.query(Table_users).filter_by(id=id).first()

    if user:
        user_dict = {
            "id": user.id ,
            "name": user.name,
            "last_name": user.last_name,
            "age": user.age}
        
        return user_dict 
    else:
        return HTTPException(status_code=404, detail="User NOT found")

# Get list of user
@router_user.get("/list_user", summary="Get list of existing Users", description="Get detailed information about existing users.")
def list_user():
    all_users = session.query(Table_users).all()
    
    list = []

    for user in all_users:
        response = {"id":user.id, "name":user.name, "last_name":user.last_name, "age":user.age}
        list.append(response)
    return list

# Update User
@router_user.put("/users/insert{id}", summary="Update a User's data", description="Update a User's values.")
def insert_user(user_id: int, user: UserUpdate):
    
    user_update = session.query(Table_users).filter_by(id=user_id).first()

    if user_update is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        for key, value in user.dict().items():
            setattr(user_update, key, value)

        session.commit()
        session.refresh(user_update)

    return user_update

# Create User
@router_user.post("/user/new", summary="Insert a new User", description="Insert a new User into the database.")
def insert_user(user: UserCreate):
    
    user_exists = session.query(Table_users).filter_by(id=user.id).first()
    
    if user_exists:
        return HTTPException(status_code=404, detail="User already exists")
    else:
        db_user = Table_users(**user.dict())
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    
    return db_user

# Delete User
@router_user.delete("/user/{user_id}", summary="Delete a User", description="Delete a User from the database.")
def delete_user(user_id:int):
    
    user_delete = session.query(Table_users).filter_by(id=user_id).first()
    
    if user_delete is None:
        return HTTPException(status_code=404, detail="User NOT found")
    else:
        session.delete(user_delete)
        session.commit()
    
    return user_delete
