# Importing essential libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np

@app.route('/')

def home():
	return render_template('main.html')

@app.route('/predict', methods=['GET','POST'])

def predict():
	
	if request.method=='POST':
       
        
        data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True)
