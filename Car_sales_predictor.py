import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('my_random_forest_regression_model.pkl', 'rb'))

def welcome():
	return "Welcome All"

def predict_selling_price(Present_Price,Kms_Driven,Owner,Model_Age,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual):
	prediction = model.predict([[Present_Price, Kms_Driven,
       Owner, Model_Age, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,Transmission_Manual]])
	print(prediction)
	return prediction

def main():
	st.title("Car Sales Predictor")
	st.write("This Web app is used to predict the reselling price of your car. Enter the information about your car below to get the predicted price.")

    #html_temp = "<div style="background-color:tomato;padding:10px"> <h2 style="color:white;text-align:center;">Streamlit Car Sales Predictor ML App </h2></div>""
    #st.markdown(html_temp, unsafe_allow_html=True)
	Present_Price = st.text_input("Purchase Price of Car (in lakhs)","Type Here")
	Kms_Driven = st.text_input("Kms Driven","Type Here")
	Owner = st.text_input("No.of Past Owners of Car","Type Here")
	Model_Age = st.text_input("Model Age (Years)","Type Here")
	Fuel_Type_Petrol= st.selectbox("Select the Fuel Type of your car",('Petrol','Diesel'))

	if (Fuel_Type_Petrol=='Petrol'):
		Fuel_Type_Petrol=1
		Fuel_Type_Diesel=0
	else:
		Fuel_Type_Petrol=0
		Fuel_Type_Diesel=1

	
	Seller_Type_Individual = st.selectbox("Choose the category of Seller",('Individual','Dealer'))

	if(Seller_Type_Individual=='Individual'):
		Seller_Type_Individual=1
	else:
		Seller_Type_Individual=0

	Transmission_Manual =  st.selectbox("Select the Type of Transmission",('Manual','Automatic'))

	if(Transmission_Manual=='Manual'):
		Transmission_Manual=1
	else:
		Transmission_Manual=0

	result=""

	if st.button("Predict"):

   		result=predict_selling_price(Present_Price,Kms_Driven,Owner,Model_Age,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual)

	st.success('The predicted price for your car is {} lakhs'.format(result))


if __name__=='__main__':
    main()