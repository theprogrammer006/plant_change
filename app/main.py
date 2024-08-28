from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .crud import get_plants, get_plant
from .models import Plant
from .database import SessionLocal, engine

# FastAPI instance
app = FastAPI()

# Pydantic model for plant selection
class PlantSelection(BaseModel):
    plant_id: int

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/plants")
async def read_plants(db: Session = Depends(get_db)):
    plants = get_plants(db)
    return plants

@app.post("/select_plant")
async def select_plant(selection: PlantSelection, db: Session = Depends(get_db)):
    plant = get_plant(db, selection.plant_id)
    if plant is None:
        raise HTTPException(status_code=404, detail="Plant not found")

    thresholds = {
        "light_threshold_min": plant.light_threshold_min,
        "light_threshold_max": plant.light_threshold_max,
        "temperature_threshold_min": plant.temperature_threshold_min,
        "temperature_threshold_max": plant.temperature_threshold_max,
        "moisture_threshold_min": plant.moisture_threshold_min,
        "moisture_threshold_max": plant.moisture_threshold_max,
    }

    # Simulate sending to the ESP32
    # esp32_url = "http://gia-smart-pot.local/update_thresholds"
    # requests.post(esp32_url, json=thresholds)

    return {"message": "Thresholds updated successfully", "thresholds": thresholds}
