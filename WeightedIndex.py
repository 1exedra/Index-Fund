url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
table = pd.read_html(url)
sp500 = table[0]
tickers = sp500['Symbol'].tolist()

start_date = '2020-01-01'
end_date = '2024-01-01'

data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
data.dropna(axis=1, inplace=True)
returns = data.pct_change()
equal_weighted_returns = returns.mean(axis=1)
equal_weighted_index = (1 + equal_weighted_returns).cumprod()

plt.figure(figsize=(10, 6))
equal_weighted_index.plot(title='Equal-Weighted S&P 500 Index')
plt.xlabel('Date')
plt.ylabel('Index Value')
plt.grid(True)
plt.show()
