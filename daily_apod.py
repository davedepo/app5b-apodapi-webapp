import streamlit as st
import requests

# api key generated on api.nasa.gov - wythsledonicdtrax@gmail.com
api_key = "TgqWQGO0YXrtlc5WvH6YJBRIxooIAgeoolZGACd8"

# api url of APOD
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# get url data as dictionary
response1 = requests.get(url)
content = response1.json()
# print(content)

# extract required data from dictionary
image_date = content["date"]
image_title = content["title"]
image_explanation = content["explanation"][:-78]
image_url = content["url"]
image_copyright = content["copyright"]


# get image as binary data
response2 = requests.get(image_url)
# print(response) # <Response [200]>

# download & write binary image data to .jpg in project dir
with open("daily_apod.jpg", "wb") as file:
	file.write(response2.content)

# set streamlit webapp layout, render image & description
st.set_page_config(layout="centered")
st.title(image_title)

st.write(f"Date: {image_date}")
st.image("daily_apod.jpg")
st.write(f"copyright: {image_copyright}")
st.write(image_url)
st.write(image_explanation)
