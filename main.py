import sys
import os

# Get the root directory path of your project
ruta_proyecto = os.path.dirname(os.path.dirname(__file__))

# Add the path to sys.path (To the root directory)
sys.path.append(ruta_proyecto)

#Package FastAPI
from fastapi import FastAPI

#Internal Module
from routers.router_product import router_product
from routers.router_user import router_user

app = FastAPI(title="REST API towards PostgreSQL",
              description="This project combines a PostgreSQL database in a Docker container with a REST API to easily enable database operations via the API.")     

#Para Ejecutar, En la terminal: uvicorn main:app --reload

app.version = "2.0.0"

app.include_router(router_user)
app.include_router(router_product)

if __name__ == "__main__":
    import subprocess

    # Especifica el host al ejecutar el comando uvicorn al iniciar el script
    subprocess.run(["uvicorn", "main:app", "--reload", "--host", "127.0.0.1"])

