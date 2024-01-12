import yfinance as yf
data = yf.download("AAPL", start="2020-01-01", end="2021-10-30")
data.to_csv('FINANCE.csv')