from sqlalchemy.orm import Session
from . import models

def get_plants(db: Session):
    return db.query(models.Plant).all()

def get_plant(db: Session, plant_id: int):
    return db.query(models.Plant).filter(models.Plant.id == plant_id).first()
