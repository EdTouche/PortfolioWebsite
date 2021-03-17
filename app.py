import streamlit as st
from PIL import Image

# Page style
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {850}px;
        padding-top: {3}rem;
        padding-right: {0}rem;
        padding-left: {0}rem;
        padding-bottom: {0}rem;
    }}
    .reportview-container .main {{
        color: {"black"};
        background-color: {"white"};
    }}
</style>
""",
        unsafe_allow_html=True,
    )

# Header
st.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;}\
     .header{padding: 10px 215px; background: #555; color: #f1f1f1; position:fixed;top:0;}\
      .sticky { position: fixed; top: 0; width: 100%;} </style>\
          <div class="header" id="myHeader">'+str("Edward Touche: Aspiring Data Analyst and Tech Consultant")+'</div>',\
               unsafe_allow_html=True)
# Image and description columns
image = Image.open("Picture.jpeg")
col1, col2 = st.beta_columns((1,3))
col1.image(image, width=200)
col2.markdown("""
# This is my portfolio site!
## Here you can find useful links to my profiles and projects!
""")

# Checkboxes for links
profiles = st.checkbox("Profiles")
if profiles:
    st.markdown("""
                **LinkedIn: https://www.linkedin.com/in/edward-touche/** \n
                **GitHub: https://github.com/EdTouche** \n
                """)

projects = st.checkbox("Projects")
if projects:
    st.markdown("""
                **Date Countdown: https://countdown2798.herokuapp.com/** \n
                **NY Taxi Fare Calculator: https://fare-calculator1298.herokuapp.com/** \n
                """)


