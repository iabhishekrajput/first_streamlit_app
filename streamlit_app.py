import streamlit
import pandas
import requests

streamlit.title('My Parent\'s New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('🍜 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
streamlit.dataframe(my_fruit_list.loc[fruits_selected])

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
