import pickle
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Initialize FastAPI Application

app = FastAPI(
    title="House Price Prediction API",
    description= "Machine Learning API to predict house prices using Linear Regression ",
    version="1.0.0"
)

# 2. Load the pre-trained ML model from the .pkl file

with open("house_model.pkl", "rb") as file:
    model = pickle.load(file)

# 3. Define Input Data Schema using Pydantic
class HouseInput(BaseModel):
    square_feet: int = Field(..., gt=100, description= "Total area in square feet of the house")
    num_rooms: int = Field(..., gt=0, description = "Total number of rooms (must be > 0)")


# 4. Define Output Data Schema using Pydantic 
class PredictionOutput(BaseModel):
    predicted_price_inr: float
    currency: str = "INR"

@app.get("/")
def home():
    return {"Status": "Online", "message": "House Price Prediction ML API is running."}

# 5. ML Prediction Endpoint

@app.post("/predict", response_model=PredictionOutput)
def predict_house_price(data: HouseInput):
    #Prepare input features in 2D format as expected by Scikit-Learn model 

    input_features = ((data.square_feet, data.num_rooms),)

    # Generate prediction using the Loaded model
    prediction = model.predict(input_features)

    # Extract the predicted value and round it to 2 decimal places
    estimated_price = round(float(prediction[0]), 2)

    return {
        "predicted_price_inr": estimated_price,
        "currency": "INR"
    }