# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:27:29 2024

@author: User
"""




import numpy as np
import pickle
import streamlit as slit
import pandas as pd


#loading the saved model
loaded_model = pickle.load(open('C:/Users/User/Desktop/ML_Projects/Multiple_Desease_Prediction/heart_disease_model.sav', 'rb'))


# creating a function for prediction

def heartDisease_prediction(input_data) :
    
    # Convert input data to a numeric type, replacing non-numeric values
    try:
        input_array = np.array(pd.to_numeric(input_data, errors='coerce'))
        if np.isnan(input_array).any():
            raise ValueError("Input contains non-numeric values or empty strings.")
    except ValueError as e:
        return str(e)
    
    # input_array = np.array(input_data)

    input_array_reshaped = input_array.reshape(1, -1)


    prediction = loaded_model.predict(input_array_reshaped)

    if (prediction[0] == 0) : return 'Not a Heart Disease Patient'
    else : return "Heart Disease Patient"
    
    
    
    
def main() :
    
    # title of the web page
    slit.title('Heart Disease Prediction Web App')
    
    # input data from the user
    col1, col2 = slit.columns(2)
    
    with col1 :
        age = slit.text_input('Age')
    with col2 :
        sex = slit.text_input('Sex')
    with col1 :
        cp = slit.text_input('Chest Pain Type')
    with col2 :
        trestbps = slit.text_input('Resting Blood Pressure')
    with col1 :
        chol = slit.text_input('Serum Cholestoral in mg/dl')
    with col2 :
        fbs = slit.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1 :
        restecg = slit.text_input('Resting Electrocardiographic Results')
    with col2 :
        thalach = slit.text_input('Maximum Heart Rate achieved')
    with col1 :
        exang = slit.text_input('Exercise Induced Angina')
    with col2 :
        oldpeak = slit.text_input('ST depression induced by exercise')
    with col1 :
        slope = slit.text_input('Slope of the peak exercise ST segment')
    with col2 :
        ca = slit.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = slit.text_input('Thal : 0 = normal; 1 = fixed defect; 2 = reversable defect')

    
    #code for prediction
    heartDisease_diagnosis = ''
    
    # creating a button for prediction
    
    if slit.button('Diabetes Test Result') : 
        heartDisease_diagnosis = heartDisease_prediction([age,	sex,	cp,	trestbps,	chol,	fbs,	restecg,	thalach,	exang,	oldpeak,	slope,	ca,	thal])
        
        slit.success(heartDisease_diagnosis)
        
if __name__ == '__main__' :
    main()
    
    
    