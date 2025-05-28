import streamlit as st
import pandas as pd
from portfolio_utils import get_portfolio_data, calculate_metrics, plot_performance

st.title("Investor Intelligence Dashboard")

tickers = st.text_input("Enter stock tickers separated by commas", "AAPL, MSFT")
weights = st.text_input("Enter weights (same order)", "0.5, 0.5")

if st.button("Analyze Portfolio"):
    ticker_list = [t.strip().upper() for t in tickers.split(',')]
    weight_list = list(map(float, weights.split(',')))

    if len(ticker_list) != len(weight_list):
        st.error("Number of tickers and weights must match.")
    else:
        try:
            df = get_portfolio_data(ticker_list)

            metrics = calculate_metrics(df, weight_list)
            st.write("Performance Metrics:", metrics)
            plot_performance(df, weight_list)

        except Exception as e:
            st.error(f"Something went wrong fetching the data: {e}")
    