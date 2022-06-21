import streamlit as st
import pandas as pd

st.title('My Parent\'s New Healthy Diner')

st.header('Breakfast Favourites')
st.text('🍜 Omega 3 & Blueberry Oatmeal')
st.text('🥬 Kale, Spinach & Rocket Smoothie')
st.text('🥚 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
st.dataframe(my_fruit_list)
