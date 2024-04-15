from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Enum("tourist", "owner_independent", "owner_employee", "admin"), default="tourist")

    profiles = relationship("Profile", back_populates="user", uselist=False)  # Assuming one-to-one for simplicity
    # Add more relationships if needed
