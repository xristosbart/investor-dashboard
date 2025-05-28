import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def get_portfolio_data(tickers, period="1y"):
    data = yf.download(tickers, period=period)["Adj Close"]
    return data

def calculate_metrics(data, weights):
    returns = data.pct_change().dropna()
    portfolio_return = returns.dot(weights)
    cumulative = (1 + portfolio_return).cumprod()

    sharpe_ratio = np.mean(portfolio_return) / np.std(portfolio_return) * np.sqrt(252)
    total_return = cumulative.iloc[-1] - 1
    cagr = (cumulative.iloc[-1])**(1/1) - 1  # assuming 1 year for now

    return {
        "Total Return": f"{total_return:.2%}",
        "CAGR": f"{cagr:.2%}",
        "Sharpe Ratio": round(sharpe_ratio, 2)
    }

def plot_performance(data, weights):
    returns = data.pct_change().dropna()
    portfolio_return = returns.dot(weights)
    cumulative = (1 + portfolio_return).cumprod()

    fig, ax = plt.subplots()
    cumulative.plot(ax=ax)
    ax.set_title("Portfolio Cumulative Return")
    st.pyplot(fig)
