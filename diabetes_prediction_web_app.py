# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:47:11 2024

@author: User
"""


import numpy as np
import pickle
import streamlit as slit


#loading the saved model
loaded_model = pickle.load(open('C:/Users/User/Desktop/ML_Projects/Multiple_Desease_Prediction/diabetes_model.sav', 'rb'))


# creating a function for prediction

def diabetes_prediction(input_data) :
    
    input_array = np.array(input_data)

    input_array_reshaped = input_array.reshape(1, -1)


    prediction = loaded_model.predict(input_array_reshaped)

    if (prediction[0] == 0) : return 'Not a Diabetic Patient'
    else : return "Diabetic Patient"
    
    
    
    
def main() :
    
    # title of the web page
    slit.title('Diabetes Prediction Web App')
    
    # input data from the user
    col1, col2 = slit.columns(2)
    
    with col1 :
        Pregnancies = slit.text_input('Value for Pregnancies')
    with col2 :
        Glucose = slit.text_input('Glucose Level')
    with col1 :
        BloodPressure = slit.text_input('Value for Blood Pressure')
    with col2 :
        SkinThickness = slit.text_input('Value for Skin Thickness')
    with col1 :
        Insulin = slit.text_input('Insulin Level')
    with col2 :
        BMI = slit.text_input('BMI value')
    with col1 :
        DiabetesPedigreeFunction = slit.text_input('Diabetes Pedigree Function value')
    with col2 :
        Age = slit.text_input('Age of the person')
    

    
    #code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if slit.button('Diabetes Test Result') : 
        diab_diagnosis= diabetes_prediction([Pregnancies,	Glucose,	BloodPressure,	SkinThickness,	Insulin,	BMI,	DiabetesPedigreeFunction,	Age])
        
        slit.success(diab_diagnosis)
        
if __name__ == '__main__' :
    main()
    
    
    