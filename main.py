import yfinance as yf

stock_symbol = input("Enter Stock Symbol (like RELIANCE.NS): ")

stock = yf.Ticker(stock_symbol)

hist = stock.history(period="5d")  # last 5 days
print(hist[['Open', 'Close', 'High', 'Low']])
import matplotlib.pyplot as plt

hist['Close'].plot(title=f"{stock_symbol} Closing Price - Last 5 Days")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()
hist.to_excel(f"{stock_symbol}_history.xlsx")
print(f"Data saved to {stock_symbol}_history.xlsx")
