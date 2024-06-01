import streamlit as st
import pandas as pd
import pickle as pk


st.title('Text Classification')
df = pd.read_csv('bbc.csv')
df

filename = 'LogisticRegression.pickle'
reg = pk.load(open(filename, 'rb'))

data = st.text_area("Enter news = ")
if st.button("Submit"):
	df = pd.DataFrame({'news':[data]})
	cat = reg.predict(df['news'])
	st.write(f"News category = {cat[0]}")