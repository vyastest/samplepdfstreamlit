import streamlit as st
import pandas as pd

# Sample DataFrame with 70 rows
data = pd.DataFrame({'Column1': range(70), 'Column2': range(100, 170)})

# Number of rows to display in each interval
rows_per_interval = 10

st.header("world cup games")
# Iterate through the DataFrame in intervals
for i in range(0, len(data), rows_per_interval):
    st.subheader(f"Table (Rows {i + 1}-{min(i + rows_per_interval, len(data))}):")
    st.write(data[i:i + rows_per_interval])

    # Add a separator to distinguish between intervals
    st.write('---')
