from fastapi import FastAPI
from pydantic import BaseModel
from streamlitt.predict import predict




app = FastAPI()

class jsonIn(BaseModel):
    postalcode: int
    property_type: str 
    property_subtype: str
    type_of_sale: str 
    living_area: float
    kitchen_type: str 
    fully_equipped_kitchen: float 
    open_fire: int
    terrace: int
    terrace_area: float
    garden: float
    garden_area: float
    surface_of_good: float
    number_of_facades: int
    swimming_pool: float
    state_of_building: str
    main_city: str
    province: str

class PredictionOut(BaseModel):
    price: float

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/predict", response_model=PredictionOut)
def predict_d(payload: jsonIn):
    
    price = predict(payload.postalcode, payload.property_type, payload.property_subtype, payload.type_of_sale, payload.living_area, payload.kitchen_type, payload.fully_equipped_kitchen, payload.open_fire, payload.terrace, payload.terrace_area, payload.garden, payload.garden_area, payload.surface_of_good, payload.number_of_facades, payload.swimming_pool, payload.state_of_building, payload.main_city, payload.province)
    return {"price": price}