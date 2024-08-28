from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    light_threshold_min = Column(Integer)
    light_threshold_max = Column(Integer)
    temperature_threshold_min = Column(Float)
    temperature_threshold_max = Column(Float)
    moisture_threshold_min = Column(Integer)
    moisture_threshold_max = Column(Integer)
