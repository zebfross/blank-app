import streamlit as st
import pandas as pd

data = {"column1": [1, 2, 3], "column2": [4, 5, 6]}
df = pd.DataFrame(data)

st.table(df)

