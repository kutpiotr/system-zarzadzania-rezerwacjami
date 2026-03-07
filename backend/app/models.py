from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    reservations = relationship("Reservation", back_populates="user")

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    reservations = relationship("Reservation", back_populates="resource")

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(String, default="pending")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)

    user = relationship("User", back_populates="reservations")
    resource = relationship("Resource", back_populates="reservations")