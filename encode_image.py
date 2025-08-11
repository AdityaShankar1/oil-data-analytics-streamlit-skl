#I wrote this script to encode the image to be made the background of my streamlit app
import base64

image_path = r"C:\Users\shank\Downloads\273402-pipeline-wallpaper-pipeline-hawaii.jpg"

with open(image_path, "rb") as img_file:
    encoded_string = base64.b64encode(img_file.read()).decode()

print(encoded_string)  # copy this string to be used in view.py