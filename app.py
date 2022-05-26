# Importing essential libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np


# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Heart Disease Predictor by Jazan student")
# st.text("1 means you've a heart disease, 0 means you don't have a heart disease")
#Age
Age = st.number_input('Age of Person')
#Sex
Sex = st.selectbox('Sex',df['sex'].unique())
#ChestPainType
cp = st.selectbox('Chest Pain Type',df['cp'].unique())
#RestingBP
trestbps = st.number_input('Resting Blood Pressure')
#Cholesterol

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        sex = request.form.get('sex')
        cp = request.form.get('cp')
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = request.form.get('exang')
        oldpeak = float(request.form['oldpeak'])
        slope = request.form.get('slope')
        ca = int(request.form['ca'])
        thal = request.form.get('thal')
        
        data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True)

