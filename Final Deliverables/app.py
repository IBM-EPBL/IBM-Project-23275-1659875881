import numpy as np 
import pickle 
import matplotlib 
import matplotlib.pyplot as plt 
import time 
import pandas 
import os 
from flask import Flask, request, jsonify, render_template
app = Flask(__name__) 
model = pickle.load(open('C:/Users/dell/OneDrive/Desktop/IBM/rainfall.pkl', 'rb')) 
scale = pickle.load(open('C:/Users/dell/OneDrive/Desktop/IBM/scale.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=[ "POST", "GET"])
def predict():
    input_feature=[x for x in request.form.values() ] 
    features_values=[np.array(input_feature)] 
    names = [["MinTemp", "MaxTemp", "Rainfall", "WindGustSpeed","Windspeed9am", "WindSpeed3pm", "Humidity9am", "Humidity 3pm", "Pressure9am", "Pressure 3pm", "Temp9am", "Temp3pm", "RainToday",
"WindGustDir", "WindDirgam", "WindDir3pm"]] 
    data = pandas.DataFrame(features_values, columns=names) 
    data = scale.fit_transform(data) 
    data = pandas.DataFrame(data, columns = names)
    prediction=model.predict(data) 
    print(prediction) 
    if prediction == [1]:
        return render_template('chance.html')
    else:
        return render_template('nochance.html')