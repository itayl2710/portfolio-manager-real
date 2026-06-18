import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portfolio Manager", layout="wide")

st.title("📊 Portfolio Manager")

st.write("Welcome to your Portfolio Manager!")

# Example: Simple portfolio display
portfolio_data = {
    "Stock": ["AAPL", "GOOGL", "MSFT"],
    "Shares": [10, 5, 8],
    "Price": [150, 140, 320]
}

df = pd.DataFrame(portfolio_data)
st.dataframe(df)

st.success("✅ App is running!")
