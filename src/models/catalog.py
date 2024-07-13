from sqlalchemy import Column, Integer, String
from .base import Base

class Agency(Base):
    __tablename__ = 'agency'
    __table_args__ = {'schema': 'test'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

class Profession(Base):
    __tablename__ = 'profession'
    __table_args__ = {'schema': 'test'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

class Ethnicity(Base):
    __tablename__ = 'ethnicity'
    __table_args__ = {'schema': 'test'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

class Gender(Base):
    __tablename__ = 'gender'
    __table_args__ = {'schema': 'test'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)