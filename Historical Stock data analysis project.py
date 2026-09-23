# =============================================================================
# 1.Imports
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
# =============================================================================
# 2.Data collection and preparation
# =============================================================================
apple = yf.download('AAPL', period='5y')
apple['Daily returns'] = apple.Close.pct_change()
AAPL_annualised_volatility = (apple['Daily returns'].std())*(np.sqrt(252))
AAPL_annualised_return = np.power((1+apple['Daily returns'].mean()),252) - 1

microsoft = yf.download('MSFT', period='5y')
microsoft['Daily returns'] = microsoft.Close.pct_change()
MSFT_annualised_volatility = (microsoft['Daily returns'].std())*(np.sqrt(252))
MSFT_annualised_return = np.power((1+microsoft['Daily returns'].mean()),252) - 1

AAPL_cumulative_growth_factor = (apple['Daily returns'] + 1).product()
MSFT_cumulative_growth_factor = (microsoft['Daily returns'] + 1).product()
apple['cumulative growth'] = (apple['Daily returns'] + 1).cumprod()
microsoft['cumulative growth'] = (microsoft['Daily returns'] + 1).cumprod()
cumulative_growth_diff = ((AAPL_cumulative_growth_factor-1)*100) - ((MSFT_cumulative_growth_factor-1)*100)

# Calculating and storing sharpe ratios, volatilities and returns of all Apple
# and Microsoft portfolios aswell as optimising for portfolio with highest sharpe
risk_free_rate = (np.power(1.04, 1/252)) - 1
correlation = apple['Daily returns'].corr(microsoft['Daily returns'], method = 'pearson')
Apple_weights = np.arange(0, 1.01, 0.01)
highest_sharpe = float('-inf')
best_weight = 0
sharpes = []
volatilities = []
returns = []
for W_a in Apple_weights:
    portfolio_volatility = np.sqrt((W_a**2)*apple['Daily returns'].std()**2 + 
                         ((1 - W_a)**2)*microsoft['Daily returns'].std()**2 +
                         2*(W_a*(1 - W_a)*apple['Daily returns'].std()*microsoft['Daily returns'].std()*correlation))
    portfolio_return = (W_a*apple['Daily returns'].mean()) + ((1 - W_a)*microsoft['Daily returns'].mean())
    portfolio_sharpe = (portfolio_return - risk_free_rate)/portfolio_volatility
    sharpes.append(portfolio_sharpe*np.sqrt(252))
    volatilities.append(portfolio_volatility*np.sqrt(252))
    returns.append(np.power((portfolio_return+1),252)-1)
    if portfolio_sharpe > highest_sharpe:
        highest_sharpe = portfolio_sharpe
        best_weight = W_a
        
#Calculating values for final analysis  
optimal_return = (best_weight*apple['Daily returns'].mean()) + ((1-best_weight)*microsoft['Daily returns'].mean())   
optimal_volatility = np.sqrt(((best_weight**2)*apple['Daily returns'].std()**2)
                             + (((1-best_weight)**2)*microsoft['Daily returns'].std()**2 +2*(best_weight*(1-best_weight)*apple['Daily returns'].std()*microsoft['Daily returns'].std()*correlation) ))
annualised_optimal_volatility = optimal_volatility*np.sqrt(252)
annualised_optimal_return = np.power((1+optimal_return),252) - 1
min_volatility = np.min(volatilities)
min_volatility_return = returns[np.argmin(volatilities)]
min_volatility_sharpe = sharpes[np.argmin(volatilities)]
best_volatility = volatilities[int(best_weight*100)]
best_return = returns[int(best_weight*100)]
min_volatility_weight = Apple_weights[np.argmin(volatilities)]
AAPL_CAGR = np.power((AAPL_cumulative_growth_factor/1), 1/5) - 1
MSFT_CAGR = np.power((MSFT_cumulative_growth_factor/1), 1/5) - 1
sharpe_portfolio_daily_returns = best_weight*apple['Daily returns'] + (1-best_weight)*microsoft['Daily returns']
sharpe_portfolio_cumulative_growth = (sharpe_portfolio_daily_returns + 1).cumprod()
sharpe_portfolio_CGF = sharpe_portfolio_cumulative_growth.iloc[-1]
sharpe_portfolio_CAGR = np.power((sharpe_portfolio_CGF/1), 1/5) - 1
volatility_portfolio_daily_returns = min_volatility_weight*apple['Daily returns'] + (1-min_volatility_weight)*microsoft['Daily returns']
volatility_portfolio_cumulative_growth = (volatility_portfolio_daily_returns + 1).cumprod()
volatility_portfolio_CGF = volatility_portfolio_cumulative_growth.iloc[-1]
volatility_portfolio_CAGR = np.power((volatility_portfolio_CGF/1), 1/5) - 1

#Finding the effecient Frontier over the entire opportunity set
sorted_indices = np.argsort(volatilities)
efficient_volatilities = []
efficient_returns = []
efficient_weights = []
highest_return = float('-inf')
for i in sorted_indices:
    if returns[i]>highest_return:
        efficient_volatilities.append(volatilities[i])
        efficient_returns.append(returns[i])
        efficient_weights.append(Apple_weights[i])
        highest_return = returns[i]      

# =============================================================================
# 3.Graphs
# =============================================================================
plt.figure()
plt.title('Apples and Microsoft Closing prices over a 5 year period')
plt.plot(apple.index, apple.Close, label='Apple')
plt.plot(microsoft.index, microsoft.Close, label='Microsoft')
plt.xlabel('date')
plt.ylabel('price($)')
plt.legend()
plt.show()

plt.figure()
plt.title('Apples and Microsofts cumulative growth (2022-2026)')
plt.plot(apple.index, apple['cumulative growth'], label = 'Apple')
plt.plot(microsoft.index, microsoft['cumulative growth'], label = 'Microsoft')
plt.xlabel('Date')
plt.ylabel('Cumulative growth factor')
plt.legend()
plt.show()

plt.figure()
plt.title('Annual portfolio sharpe ratio vs weight of Apple stocks')
plt.plot(Apple_weights, sharpes)
plt.xlabel('Weight of Apple stocks')
plt.ylabel('Daily portfolio Sharpe ratio')
plt.show()

plt.figure()
plt.title('Portfolio Risk vs Portfolio Return')
plt.scatter(volatilities,returns, label = 'Opprtunity set')
plt.scatter(efficient_volatilities,efficient_returns, label = 'Efficient Frontier', alpha = 0.4, s = 15)
plt.scatter(volatilities[np.argmin(volatilities)],returns[np.argmin(volatilities)], label = 'Portfolio with lowest volatility') 
plt.scatter(volatilities[int(best_weight*100)],returns[int(best_weight*100)], label = 'portfolio with highest sharpe ratio')
plt.xlabel('Annualised Volatility')
plt.ylabel('Annnualised Return')
plt.legend()
plt.show() 
# =============================================================================
# 4.Summary/Comparison Table
# =============================================================================
data = {
    'Portfolio': ['Apple','Microsoft','Minimum Volatility','Highest sharpe'],
    'Apple Weight': ['100','0',int((min_volatility_weight*100)),int(best_weight*100)],
    'Microsoft Weight': ['0','100',int(((1-min_volatility_weight)*100)),100-int(best_weight*100)],
    'Annualised Return': [AAPL_annualised_return,MSFT_annualised_return,min_volatility_return,best_return],
    'Annualised Volatility': [AAPL_annualised_volatility,MSFT_annualised_volatility,min_volatility,best_volatility],
    'Sharpe Ratio': [sharpes[100],sharpes[0],min_volatility_sharpe,highest_sharpe*np.sqrt(252)],
    'CAGR': [AAPL_CAGR,MSFT_CAGR,volatility_portfolio_CAGR,sharpe_portfolio_CAGR]
}
comparison_df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
print(comparison_df)
