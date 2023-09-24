from pydantic import BaseModel

# Definition of models

class ProductCreate(BaseModel):
    code: str
    product_name: str
    stock: int
    price: float

class ProductUpdate(BaseModel):
    product_name: str
    stock: int
    price: float

class ProductrOut(BaseModel):
    code: str
    product_name: str
    stock: int
    price: float