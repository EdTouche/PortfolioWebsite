import streamlit as st
from PIL import Image

# Tab config
st.set_page_config(
    page_title="Edward Touche",
    page_icon="",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

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
     .header{padding: 10px 218px; background: #555; color: #f1f1f1; position:fixed;top:0;}\
      .sticky { position: fixed; top: 0; width: 100%;} </style>\
          <div class="header" id="myHeader">'+str("Edward Touche: Aspiring Data Analyst and Tech Consultant")+'</div>',\
               unsafe_allow_html=True)

# Image and bio columns
image = Image.open("Picture.jpeg")
col1, col2 = st.beta_columns((1,3))
col1.image(image, width=200)
col2.markdown("""
    # Welcome to my site!
    I am an aspiring data analyst and technology consultant, with a keen
    passion in all things technology. Since graduating into a pandemic, I 
    have spent my time gathering skills and qualifications. I have become very 
    proficient at Python for data science, analytics, machine and deep learning. 
    That combined with my, Google Analytics Basic and Advanced qualifications, 
    knowledge of SPSS and statistics and my familiarity of Office365
    I am an ideal candidate for any data analyst and technology consultant roles!
""")

# Links line
st.markdown(""" 
### Here you can find useful links to my profiles and projects!
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


