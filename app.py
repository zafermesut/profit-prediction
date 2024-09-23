import streamlit as st
import joblib


# Load the model
model = joblib.load('model.joblib')

def predict_profit(RD_Spend, Administration, Marketing_Spend):
    input_data = [RD_Spend, Administration, Marketing_Spend]
    input_data = [float(i) for i in input_data]
    input_data = [input_data]
    prediction = model.predict(input_data)
    return prediction[0]

st.title('Profit Prediction App')

RD_Spend = st.text_input('Enter R&D Spend')
Administration = st.text_input('Enter Administration')
Marketing_Spend = st.text_input('Enter Marketing Spend')

if st.button('Predict'):
    profit = predict_profit(RD_Spend, Administration, Marketing_Spend)
    st.success(f'The profit is {profit}')