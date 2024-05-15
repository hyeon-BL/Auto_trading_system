import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px  # interactive charts
import pyupbit
import time

st.markdown("# Bitcoin Price App")
st.markdown("Welcome to the Bitcoin Price App! Here, you can check the price of Bitcoin in real-time.")

st.markdown("## Bitcoin Price Data")
st.markdown("Here is the data of Bitcoin price.")
data = []
chart = st.empty()  # Create an empty chart
idx = 0
viewLimit = 60
while True:
    try:
        d = pyupbit.get_current_price("KRW-BTC")
        if len(data) == viewLimit:
            data.pop(0)  # Remove the first element
        data.append(d)
        idx += 1
        time.sleep(1)
        print(data)
        chart.line_chart(data)  # Update the chart
    except:
        pass

# df = pd.DataFrame(data, columns=['trade_price', 'trade_volume', 'timestamp'])
# st.dataframe(df)