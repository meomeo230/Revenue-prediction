import streamlit as st
import pickle

nu = st.number_input('Input Temperature')
st.title('Revenue Prediction')
model = pickle.load(open('model.pickle', "rb"))

if st.button('Predict'):
    st.write("Revenue Prediction")
    st.code(float(model.predict([[nu]])))
