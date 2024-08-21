import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title = "My webpage", page_icon =":tada:", layout = "wide")

image1 = Image.open("Oscars.jpg")
image2 = Image.open("Cilian.jpg")

left_column, right_column = st.columns(2)

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options=["Introduction", "List of winners", "Sources"],
    )

if selected == "Introduction":
    st.subheader("A Short Project")
    st.title("The Oscars")
    st.write("By Vishal Ramesh") 
    st.write("---")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("An Introduction")
            st.write("""Hello there,
                this is a little website I made as a test regarding the theme, the Oscars. Some notable awards of the Oscars include:
               
                Best Motion Picture
            
                Best Choreography
            
                Best Music
            
                and so much more... """)
        with right_column: 
            st.image(image1, caption = "The Oscars Trophy", width = 400)
if selected == "List of winners":
    with left_column: 
        st.header("List of Winners")
        st.write("---")
        st.write("""
                Best Actor in a Leading role:

                2023 - Cilian Murphy
                
                2022 - Brendan Fraser
                
                2022 - Will Smith 
                
                2021 - Anthony Hopkins
                
                2020 - Joaquin Phoenix 
                
                ...""")
    with right_column:
        st.image(image2, caption = "Cilian winning his award", width = 400)

if selected == "Sources":
    st.header("Sources")
    st.write("Wikipedia")