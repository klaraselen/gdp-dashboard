import streamlit as st
from PIL import Image 

# Set the title of the app
st.title("🎈 Upload a nice photo for funsies!")

# Allow user to upload an image
uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Check if an image is uploaded
if uploaded_image is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_image)
    
    # Display the image
    st.image(image, caption="Your fun photo!", use_column_width=True)
else:
    st.write("Please upload an image to get started!")
