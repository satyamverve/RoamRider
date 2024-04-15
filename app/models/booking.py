from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    bike_id = Column(Integer, ForeignKey('bikes.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    total_cost = Column(Float)

    bike = relationship("Bike")
    user = relationship("User")
