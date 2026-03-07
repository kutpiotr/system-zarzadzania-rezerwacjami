from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=schemas.ReservationResponse)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_reservation(db, reservation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.ReservationResponse])
def get_reservations(db: Session = Depends(get_db)):
    return crud.get_reservations(db)