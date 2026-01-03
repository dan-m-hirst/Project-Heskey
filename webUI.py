import streamlit as st
from time import sleep
import random
import pandas as pd
#need to run in terminal "streamlit run webUI.py"
#random.shuffle to randomise list
sponsor_list = list(pd.read_csv("Simulator Files/sponsors.csv", header = False))
sponsor = random.choice(sponsor_list)

st.title(f"Patented Mike Dixon 4most Draw Simulator - brought to you by {sponsor}")
st.write("Hello World!")

st.set_page_config(layout="wide")

if st.button("Run"):
    #we want to run all of our procedural dialogue and draw in here
    st.write("Button active")
    sleep(3)
    st.write("Delay test successful")
    with st.empty():
        st.write("this container is used for")
        sleep(3)
        st.write("overwriting text instead of simply printing downwards")
    pass