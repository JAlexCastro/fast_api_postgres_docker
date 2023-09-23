# Models from FastAPI
from fastapi import FastAPI, HTTPException

# Internals Models
from models.models_user import UserCreate, UserUpdate, UserOut
from tables.table_user import Table_users
from conection import session


app = FastAPI(title="API Rest de practica")

# Get User by ID
@app.get("/user{user_id}")
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
@app.get("/list_user")
def list_user():
    all_users = session.query(Table_users).all()
    
    list = []

    for user in all_users:
        response = {"id":user.id, "name":user.name, "last_name":user.last_name, "age":user.age}
        list.append(response)
    return list

# Update User
@app.put("/users/insert{id}")
def insert_user(user_id: int, user: UserCreate):
    
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
@app.post("/user/new")
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
@app.delete("/user/{user_id}")
def delete_user(user_id:int):
    
    user_delete = session.query(Table_users).filter_by(id=user_id).first()
    
    if user_delete is None:
        return HTTPException(status_code=404, detail="User NOT found")
    else:
        session.delete(user_delete)
        session.commit()
    
    return user_delete
