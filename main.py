import streamlit as st
import requests
from config import api_key

url = "https://api.nasa.gov/planetary/apod?api_" \
      f"key={api_key}"

request = requests.get(url)
content = request.json()

title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

response = requests.get(image_url)
image_filepath = "nasa_pic.jpg"
with open(image_filepath, "wb") as file:
    file.write(response.content)


st.header(title)
st.image(image_filepath)
st.write(explanation)