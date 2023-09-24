from pydantic import BaseModel

# Definition of models


class UserCreate(BaseModel):
    id: int
    name: str
    last_name: str
    age: int

class UserUpdate(BaseModel):
    name: str
    last_name: str
    age: int
