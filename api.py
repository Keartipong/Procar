from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Car(BaseModel):
    id: int
    license_plate: str
    

# Database mock (in-memory list)
database = []

@app.post("/cars/", response_model=Car)
async def create_car(car: Car):
    database.append(car)
    return car

@app.get("/cars/", response_model=List[Car])
async def get_cars():
    return database

@app.get("/cars/{car_id}", response_model=Car)
async def get_car(car_id: int):
    for car in database:
        if car.id == car_id:
            return car
    return {"error": "Car not found"}

@app.put("/cars/{car_id}", response_model=Car)
async def update_car(car_id: int, car: Car):
    for idx, existing_car in enumerate(database):
        if existing_car.id == car_id:
            database[idx] = car
            return car
    return {"error": "Car not found"}

@app.delete("/cars/{car_id}", response_model=Car)
async def delete_car(car_id: int):
    for idx, existing_car in enumerate(database):
        if existing_car.id == car_id:
            deleted_car = database.pop(idx)
            return deleted_car
    return {"error": "Car not found"}