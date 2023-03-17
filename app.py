import pickle

nu = st.number_input('Input Temperature')
st.title('Revenue Prediction')

if st.button('Predict'):
    st.write("Revenue Prediction")
    st.code(float(model.predict([[nu]])))
