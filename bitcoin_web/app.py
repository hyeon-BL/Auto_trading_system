import streamlit as st
import pandas as pd
import pyupbit

# st.markdown("# Bitcoin Price App")
# st.markdown("Welcome to the Bitcoin Price App! Here, you can check the price of Bitcoin in real-time.")

# st.markdown("## Bitcoin Price Data")
# st.markdown("Here is the data of Bitcoin price.")
data = pyupbit.get_current_price("KRW-BTC", "KRW-ETH", "KRW-XRP")
print(data)