from collections import namedtuple
#from winreg import ExpandEnvironmentStrings
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

expenses = income * (1-saving_rate)
investment = income - expenses
annual_return = investment * interest_rate
year = 2022
withdrawal_rate = 0.04

Year = []
Yearly_Income = []
Yearly_Expenses = []
Yearly_Invested_Amount = []
Total_Invested_Amount = []
Annual_Returns = []

Year.append(year)
Yearly_Income.append(income)
Yearly_Expenses.append(expenses)
Yearly_Invested_Amount.append(income - expenses)
Total_Invested_Amount.append(investment)
Annual_Returns.append(annual_return)

invested_years = 30
for i in range(0, invested_years -1):
    investment = (income - expenses) + annual_return + investment
    annual_return = investment * interest_rate
    Year.append(year + i + 1)
    Yearly_Income.append(income)
    Yearly_Expenses.append(expenses)
    Yearly_Invested_Amount.append(income - expenses)
    Total_Invested_Amount.append(investment)
    Annual_Returns.append(annual_return)

st.text(annual_return)