from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def create_resource(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(name=resource.name, type=resource.type)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

def get_resources(db: Session):
    return db.query(models.Resource).all()

def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    if reservation.end_time <= reservation.start_time:
        raise ValueError("Data konca musi byc pozniejsza niz data poczatku")

    conflicting_reservation = db.query(models.Reservation).filter(
        models.Reservation.resource_id == reservation.resource_id,
        models.Reservation.start_time < reservation.end_time,
        models.Reservation.end_time > reservation.start_time
    ).first()

    if conflicting_reservation:
        raise ValueError("Ten zasob jest juz zarezerwowany w tym czasie")

    db_reservation = models.Reservation(
        start_time=reservation.start_time,
        end_time=reservation.end_time,
        user_id=reservation.user_id,
        resource_id=reservation.resource_id
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservations(db: Session):
    return db.query(models.Reservation).all()