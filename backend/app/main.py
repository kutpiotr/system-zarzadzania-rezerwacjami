from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, resources, reservations
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="System Zarzadzania Rezerwacjami")

app.include_router(users.router)
app.include_router(resources.router)
app.include_router(reservations.router)

@app.get("/")
def read_root():
    return {"message": "API dziala"}