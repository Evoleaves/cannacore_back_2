
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

class Variety(Base):
    __tablename__ = "varieties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    mothers = relationship("Mother", back_populates="variety")

class Mother(Base):
    __tablename__ = "mothers"

    id = Column(Integer, primary_key=True, index=True)
    variety_id = Column(Integer, ForeignKey("varieties.id"))
    code = Column(String, nullable=False)

    variety = relationship("Variety", back_populates="mothers")
    plants = relationship("Plant", back_populates="mother")
    lots = relationship("Lot", back_populates="mother")

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    mother_id = Column(Integer, ForeignKey("mothers.id"))
    code = Column(String, nullable=False)

    mother = relationship("Mother", back_populates="plants")

class Lot(Base):
    __tablename__ = "lots"

    id = Column(Integer, primary_key=True, index=True)
    variety_id = Column(Integer, ForeignKey("varieties.id"))
    mother_id = Column(Integer, ForeignKey("mothers.id"))
    code = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    plant_count = Column(Integer)

    mother = relationship("Mother", back_populates="lots")
    variety = relationship("Variety")
