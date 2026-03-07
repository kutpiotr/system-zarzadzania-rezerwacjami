from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import users, resources, reservations
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="System Zarzadzania Rezerwacjami")

app.add_middleware(
CORSMiddleware,
allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(resources.router)
app.include_router(reservations.router)

@app.get("/")
def read_root():
    return {"message": "API dziala"}