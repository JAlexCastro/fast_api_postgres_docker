import sys
import os

# Get the root directory path of your project
ruta_proyecto = os.path.dirname(os.path.dirname(__file__))

# Add the path to sys.path (To the root directory)
sys.path.append(ruta_proyecto)




# Internal models
from tables.table_products import Table_products
from schemas.schemas_product import ProductCreate, ProductUpdate, ProductrOut
from connection import session

# FastAPI modules
from fastapi import APIRouter, HTTPException

router_product = APIRouter()


# Get Product by CODE
@router_product.get("/prodect{product_code}", summary="Get Product by CODE", description="Get information from an existing User")
def get_product(product_code:str):

    product = session.query(Table_products).filter_by(code=product_code).first()

    if product:
        product_dict = {
            "code": product.code ,
            "product_name": product.product_name,
            "stock": product.stock,
            "price": product.price}
        
        return product_dict 
    else:
        return HTTPException(status_code=404, detail="Product NOT found")

# Get list of Product
@router_product.get("/product/list", summary="Get list of existing Product", description="Get detailed information about existing Product.")
def list_product():
    all_product = session.query(Table_products).all()
    
    list = []

    for product in all_product:
        response = {"code":product.code, "product_name":product.product_name, "stock":product.stock, "price":product.price}
        list.append(response)
    return list

# Update Product
@router_product.put("/product/insert{product_code}", summary="Update a Product's data", description="Update a Product's values.")
def update_product(product_code: str, product: ProductUpdate):
    
    product_update = session.query(Table_products).filter_by(code=product_code).first()

    if product_update is None:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        for key, value in product.dict().items():
            setattr(product_update, key, value)

        session.commit()
        session.refresh(product_update)

    return product_update

# Create Product
@router_product.post("/product/new", summary="Insert a new Product", description="Insert a new Product into the database.")
def insert_product(product: ProductCreate):
    
    product_exists = session.query(Table_products).filter_by(code=product.code).first()
    
    if product_exists:
        return HTTPException(status_code=404, detail="Product already exists")
    else:
        try:
            product_insert = Table_products(**product.dict())
            session.add(product_insert)
            session.commit()
            session.refresh(product_insert)
        except Exception:
            return HTTPException(status_code=500, detail="Internal Server Error: Error creating product")
    return product_insert

# Delete Product
@router_product.delete("/product/{product_code}", summary="Delete a Product", description="Delete a Product from the database.")
def delete_product(product_code:str):
    
    product_delete = session.query(Table_products).filter_by(code=product_code).first()
    
    if product_delete is None:
        return HTTPException(status_code=404, detail="Product NOT found")
    else:
        try:
            session.delete(product_delete)
            session.commit()
        except Exception:
            return HTTPException(status_code=500, detail="Internal Server Error: Could not delete product")
    return product_delete
