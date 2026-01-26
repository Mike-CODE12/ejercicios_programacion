from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False, unique=True)

    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    cars = relationship("Car", back_populates="user") 


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String(120), nullable=False)
    city = Column(String(80), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    user = relationship("User", back_populates="addresses")


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    make = Column(String(60), nullable=False)
    model = Column(String(60), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  
    user = relationship("User", back_populates="cars")
