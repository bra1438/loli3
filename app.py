import streamlit as st
import numpy as np
import pickle

# Load the trained models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.set_page_config(page_title='Disease Prediction App', page_icon=':hospital:')

# Define the function for diabetes prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = diabetes_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

# Define the Streamlit app
def main():
    st.title('Designed and developed by :  Abdelkarim  / Diabetes Prediction System using Artificial Intelligence')
    # Display input fields for diabetes prediction
    st.subheader('A Diabetes Prediction System using Artificial Intelligence (AI) is a computer program that uses machine learning algorithms to analyze patient data and predict whether they have diabetes or not. These systems can be used to help doctors diagnose diabetes early and make informed treatment decisions.')
    image = 'diabetes.png'  # Replace with the path to your image
    st.image(image, width=500)
    age = st.slider('Age of the person', min_value=0, step=1, value=0)
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1, value=0)
    glucose = st.number_input('Amount of Blood Glucose Level', min_value=0.0, step=1.0, value=0.0)
    blood_pressure = st.number_input('Blood Pressure Value', min_value=0.0, step=1.0, value=0.0)
    skin_thickness = st.number_input('Skin Thickness Value', min_value=0.0, step=1.0, value=0.0)
    insulin = st.number_input('Insulin Level', min_value=0.0, step=1.0, value=0.0)
    bmi = st.number_input('Body Mass Index Value', min_value=0.0, step=1.0, value=0.0)
    diabetes_pedigree = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, step=0.01, value=0.0)
    age = st.slider('Age of the person', min_value=0, step=1, value=0)
    

    # When the user clicks the 'Predict' button, make the diabetes prediction
    if st.button('Predict'):
            input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
            prediction = diabetes_prediction(input_data)
            st.write(prediction)


# Run the Streamlit app
if __name__ == '__main__':
    main()

