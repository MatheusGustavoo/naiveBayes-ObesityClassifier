from flask import Flask, request, jsonify
from pydantic import BaseModel
from flask_pydantic import validate
import joblib
import pandas as pd

# Create a Flask app
app = Flask(__name__)

# Classe que recebera os dados dos formula

class request_data(BaseModel):
    Gender: int
    Age: int
    Height: int
    Weight: int
    family_history_with_overweight: int
    FAVC: int
    FCVC: int
    NCP: int
    CAEC: int
    SMOKE: int
    CH2O: int
    SCC: int
    FAF: int
    TUE: int
    CALC: int
    MTRANS: int

obesity_model = joblib.load('obesity_model.pkl')

@app.route('/predict', methods=['POST'])
@validate()
def predict(body: request_data):
    