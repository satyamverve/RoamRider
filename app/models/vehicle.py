from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Bike(Base):
    __tablename__ = 'bikes'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('bike_owners.id'))
    status = Column(Enum("available", "booked"), default="available")
    current_location = Column(String)

    owner = relationship("BikeOwner", back_populates="bikes")
