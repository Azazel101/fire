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
    "saving rate",
    min_value=0.0,
    max_value=1.0,
    step=0.01,
    value=0.5,
    help="You can choose the number of keywords/keyphrases to display. Between 0 and 1, default number is 0.5.",
)

income = st.slider(
    "income",
    min_value=100,
    max_value=50000,
    step=10,
    value=1000,
    help="You can choose the number of keywords/keyphrases to display. Between 100 and 50000, default number is 10.",
)

interest_rate = st.slider(
    "interest rate",
    min_value=0.0,
    max_value=1.0,
    step=0.01,
    value=0.5,
    help="You can choose the number to display. Between 0 and 1, default number is 0.5.",
)