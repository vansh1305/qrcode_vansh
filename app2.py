import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import qrcode

html_code = """
        <div style="background-color: #1abc9c; padding:  10px; border-radius: 10px">
          <h1 style="color:white; text-align: center">QR Code Generator</h1>
        </div>
        """
components.html(html_code)     

# Image
img = Image.open("qrcode.jpg")
st.image(img, width = 700)

data = st.text_input("Enter your data that you want ot embed")

box_size = st.number_input("Enter box size:")
border = st.number_input("Enter border spacing:")

from matplotlib import colors as mcolors

colors = mcolors.CSS4_COLORS

colors_list = list(colors.keys())

fill = st.selectbox("Select the fill color", colors_list)
back = st.selectbox("Select the back color", colors_list)


if(st.button("Generate QR Code")):
    qr = qrcode.QRCode(box_size = box_size, border = border)
    
    qr.add_data(data)
    qr.make()
    
    img = qr.make_image(fill_color = fill,
                        back_color = back)

    img.save('myqr.png')
    
    img = Image.open("myqr.png")
    st.image(img)













