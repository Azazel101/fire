from collections import namedtuple
#from winreg import ExpandEnvironmentStrings
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime


"""
# FIRE (Financial Independence, Retire Early)

"""

#st.write("Toto je test.")

saving_rate = st.slider(
    "Saving rate",
    min_value=0.0,
    max_value=1.0,
    step=0.01,
    value=0.5,
    help="You can choose the number of keywords/keyphrases to display. Between 0 and 1, default number is 0.5.",
)

income = st.slider(
    "Yearly Income",
    min_value=5000,
    max_value=50000,
    step=10,
    value=18000,
    help="You can choose the number of keywords/keyphrases to display. Between 100 and 50000, default number is 10.",
)

interest_rate_raw = st.slider(
    "interest rate",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    value=8.0,
    help="You can choose the number to display. Between 0 and 1, default number is 0.5.",
)

interest_rate = interest_rate_raw / 100

expenses = income * (1-saving_rate)
investment = income - expenses
annual_return = investment * interest_rate
year = datetime.now().year
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

df = pd.DataFrame()
df['Year'] = Year
df['Yearly_Income'] = Yearly_Income
df['Yearly_Expenses'] = Yearly_Expenses
df['Yearly_Invested_Amount'] = Yearly_Invested_Amount
df['Total_Invested_Amount'] = Total_Invested_Amount
df['Annual_Returns'] = Annual_Returns
Yearly_Withdrawal_Amount = np.array(Total_Invested_Amount) * withdrawal_rate
df['Yearly_Withdrawal_Amount'] = Yearly_Withdrawal_Amount
df.set_index('Year')

df_graph = pd.DataFrame()
df_graph['Yearly_Expenses'] = Yearly_Expenses
df_graph['Yearly_Withdrawal_Amount'] = Yearly_Withdrawal_Amount

st.write(df[df.Yearly_Expenses <= df.Yearly_Withdrawal_Amount].head(1))


st.dataframe(df)
st.line_chart(df_graph)

st.write("Calculate the income amount wanted given som average yearly interest rate and your current principle.")
st.write("Vypočítajte si požadovanú výšku príjmu vzhľadom na priemernú ročnú úrokovú sadzbu a váš aktuálny princíp.")

principle = st.number_input("What is your principle amount?")
interest_rate_raw_1 = st.slider(
    "interest rate 1",
    min_value=0.0,
    max_value=100.0,
    step=0.1,
    value=8.0,
    help="You can choose the number to display. Between 0 and 1, default number is 0.5.",
)

amount = principle * (interest_rate_raw_1 / 100)
st.write("You would make on average:", amount, "per year")

st.write("Calculate the principle you need given some average yearly interest rate to make x income")
st.write("Vypočítajte si princíp, ktorý potrebujete vzhľadom na nejakú priemernú ročnú úrokovú sadzbu, aby ste dosiahli x výšku príjmu za rok.")

interest_rate_raw_2 = st.number_input("What is your averagte yearly interest rate percentage (%)?",value=4.0, step=0.1)
amount_1 = st.number_input("What is the amount per year that you want to make from that interest rate ?",value=10000)

principle = amount_1 / ((interest_rate_raw_2) / 100)
st.write("You would need a princle of about", principle, "to have an annual income of", amount_1,"% interest yearly from your principle.")

st.write("Calculate the average yearly interest rate you need given some principle amount to make x income amount per year.")
st.write("Vypočítajte priemernú ročnú úrokovú sadzbu, ktorú potrebujete vzhľadom na nejakú zásadnú sumu, aby ste dosiahli x výšku príjmu za rok.")

principle_1 = st.number_input("What is your principle amount?",value=10000)
amount_2 = st.number_input("What is the amount per year that you want to make from that interest rate ?",value=10000)

interest_rate = amount_2 / principle_1 * 100

st.write("You would need to find an asset or investment that gives an average of", interest_rate, "% interest per year.")
