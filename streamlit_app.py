from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

"""

st.write("Toto je test.")

saving_rate = st.slider(
    "# of results",
    min_value=0.0,
    max_value=1.0,
    step=0.01,
    value=0.5,
    help="You can choose the number of keywords/keyphrases to display. Between 0 and 1, default number is 0.5.",
)
