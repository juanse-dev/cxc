from sqlalchemy import Column, Integer, String, BigInteger, Numeric, DateTime, ForeignKey, func
from .base import Base
from config import Config

print(Config.SCHEMA)
class Agency(Base):
    __tablename__ = 'agency'
    __table_args__ = {'schema': Config.SCHEMA}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Profession(Base):
    __tablename__ = 'profession'
    __table_args__ = {'schema': Config.SCHEMA}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Ethnicity(Base):
    __tablename__ = 'ethnicity'
    __table_args__ = {'schema': Config.SCHEMA}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Gender(Base):
    __tablename__ = 'gender'
    __table_args__ = {'schema': Config.SCHEMA}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Employee(Base):
    __tablename__ = 'employee'
    __table_args__ = {'schema': Config.SCHEMA}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    agency_id = Column(Integer, ForeignKey(f"{Config.SCHEMA}.agency.id"), nullable=False)
    profession_id = Column(Integer, ForeignKey(f"{Config.SCHEMA}.profession.id"), nullable=False)
    gender_id = Column(Integer, ForeignKey(f"{Config.SCHEMA}.gender.id"), nullable=False)
    ethnicity_id = Column(Integer, ForeignKey(f"{Config.SCHEMA}.ethnicity.id"), nullable=False)
    monthly_salary = Column(Numeric(16, 2), nullable=False)
    md5 = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)