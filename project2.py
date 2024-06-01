import numpy as np
import pandas as pd
import streamlit as st

import pickle as pk

st.title('Salary Prediction System')
filename = 'LinearRegression.pickle'
reg = pk.load(open(filename, 'rb'))

#taking input from user
age = st.number_input("Age", 20, 60)
exp = st.number_input("Experience", 0, 40)
edu = st.radio("Education", ["Bachelor's", "Master's","PhD"])
st.write(age,exp,edu)
if edu == "Bachelor's":
	e1 = 1
else:
	e1 = 0
if edu == "Master's":
	e2 = 1
else:
	e2 = 0

if edu == "PhD":
	e3 = 1
else:
	e3 = 0

if st.button("submit"):

	data = {'Age':[age],
	        'Years of Experience':[exp],
	        "Bachelor's":[e1],
	        "Master's":[e2],
	         "PhD":[e3]}

	df = pd.DataFrame(data)
	df
	predicted_salary = reg.predict(df)
	st.write("Predicted Salary",predicted_salary)
# print("Predicted Salary using Polynomial regression",pol_reg.predict(poly_reg.fit_transform(data)))-