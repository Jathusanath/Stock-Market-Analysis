# Historical Stock Market Data Analysis with Python 
## Overview
This project analyses historical stock market data for Apple and Microsoft using Python. The project investigates stock returns, volatility and risk-adjusted performance for individual stocks as well as two-asset portfolios and finally analyses the efficient frontier.
## Data
Historical stock price data for Apple and Microsoft is obtained from Yahoo Finance using the 'yfinance' library in python. The analysis uses a five year period of historical data.
## Methodology
The analysis includes:
  -Daily stock returns
  -Annualised returns 
  -Annualised Volatility
  -Cumulative returns
  -sharpe ratios
  -Pearson correlation
  -Two-asset portfolio construction
  -Portfolio optimisation
  -Minimum volatility portfolio
  -Maximum Sharpe Ratio portfolio
  -Efficient Frontier 
  -CAGR
## Results
| Portfolio          |   Apple Weight |   Microsoft Weight |   Annualised Return |   Annualised Volatility |   Sharpe Ratio |     CAGR |
|:-------------------|---------------:|-------------------:|--------------------:|------------------------:|---------------:|---------:|
| Apple              |            100 |                  0 |            0.235254 |                0.280561 |       0.613563 | 0.186703 |
| Microsoft          |              0 |                100 |            0.163169 |                0.282223 |       0.396744 | 0.117386 |
| Minimum Volatility |             51 |                 49 |            0.199393 |                0.246106 |       0.579659 | 0.162833 |
| Highest sharpe     |             85 |                 15 |            0.224164 |                0.263368 |       0.619347 | 0.181567 |

Apple had a higher CAGR and return compared to Microsoft over the five year period. The individual Apple stock had the highest return while the 85/15 portfolio had the highest Sharpe which suggests that this portfolio had a higher risk adjusted performance. Additionally, combining the two stocks of Apple and Microsoft resulted in a lower volatility compared to the individual stocks which highlights the diversification effect.
## Limitations
This analysis is based on historical data (a 5 year period) so cannot be used to ascertain future performance. The analysis only investigates two asses and does not account for factors such as transaction cost, dividends or taxes. Therefore, the portfolio optimisation is intended to explore risk and return rather than real world investment.
## Technologies
Python: data analysis and portfolio calculations
NumPy: numerical calculations and array operations
pandas: data manipulation and analysis
Matplotlib: data visualisation
yfinance: retrieval of historical stock market data
Git and GitHub: version control and project hosting
