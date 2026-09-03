import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
apple = yf.download('AAPL', period='5y')
# print(apple.head())
# print(apple.info())
# print(apple.describe())
# print(apple.Close.agg(['max','min','mean']))
# plt.title('Apples Closing prices over a 5 year period')
# plt.plot(apple.index, apple.Close)
# plt.xlabel('date')
# plt.ylabel('price($)')
# plt.show()
apple['Daily returns'] = apple.Close.pct_change()
# print(apple['Daily returns'].head())
# print(apple['Daily returns'].describe())
AAPL_annualised_volitility = (apple['Daily returns'].std())*(np.sqrt(252))
# print(AAPL_annualised_volitility)

microsoft = yf.download('MSFT', period='5y')
# plt.title('Microsofts Closing orices over a 5 year period')
# plt.plot(microsoft.index, microsoft.Close)
# plt.xlabel('date')
# plt.ylabel('price ($)')
microsoft['Daily returns'] = microsoft.Close.pct_change()
# print(microsoft['Daily returns'].head())
# print(microsoft['Daily returns'].describe())
MSFT_annualised_volatility = (microsoft['Daily returns'].std())*(np.sqrt(252))
# print(MSFT_annualised_volatility)

AAPL_cumulative_growth_factor = (apple['Daily returns'] + 1).product()
# print(AAPL_cumulative_growth_factor)
MSFT_cumulative_growth_factor = (microsoft['Daily returns'] + 1).product()
# print(MSFT_cumulative_growth_factor)
# print((AAPL_cumulative_growth_factor-1)*100)
# print((MSFT_cumulative_growth_factor-1)*100)

apple['cumulative growth'] = (apple['Daily returns'] + 1).cumprod()
# print(apple[['Daily returns','cumulative growth']].head())
microsoft['cumulative growth'] = (microsoft['Daily returns'] + 1).cumprod()
# plt.title('Apples and Microsofts cumulative growth (2022-2026)')
# plt.plot(apple.index, apple['cumulative growth'], label = 'Apple')
# plt.plot(microsoft.index, microsoft['cumulative growth'], label = 'Microsoft')
# plt.xlabel('Date')
# plt.ylabel('Cumulative growth factor')
# plt.legend()
cumulative_growth_diff = ((AAPL_cumulative_growth_factor-1)*100) - ((MSFT_cumulative_growth_factor-1)*100)
# print(cumulative_growth_diff)

risk_free_rate = (np.power(1.04, 1/252)) - 1
# print(risk_free_rate)
# print(((apple['Daily returns'] - risk_free_rate).mean())/apple['Daily returns'].std())
print(apple['Daily returns'])






