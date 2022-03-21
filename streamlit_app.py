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