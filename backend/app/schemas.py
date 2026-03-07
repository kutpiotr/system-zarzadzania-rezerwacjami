from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class ResourceCreate(BaseModel):
    name: str
    type: str

class ResourceResponse(BaseModel):
    id: int
    name: str
    type: str

    class Config:
        from_attributes = True

class ReservationCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    user_id: int
    resource_id: int

class ReservationResponse(BaseModel):
    id: int
    start_time: datetime
    end_time: datetime
    status: str
    user_id: int
    resource_id: int

    class Config:
        from_attributes = True