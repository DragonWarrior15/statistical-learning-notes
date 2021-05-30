import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import pacf, acf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.gofplots import qqplot
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.diagnostic import acorr_ljungbox

# read the data and get its structure
df = pd.read_csv('USAccDeaths.csv')
# The values for the first six months of 1979 are 7798 7406 8363 8460 9217 9316
print(df.columns) # Index(['time', 'USAccDeaths'], dtype='object')
print(df.shape) # (72,2)

# check the plot of the whole timeseries
plt.plot(df['USAccDeaths'].values)
plt.show()

# there is periodicity, remove it by differencing
df['diff12'] = df['USAccDeaths'] - df['USAccDeaths'].shift(12)
plt.plot(df['diff12'].values)
plt.show()

# remove the trend by differencing
df['diff12_1'] = df['diff12'] - df['diff12'].shift(1)

# this is an almost stationary series, continue analysis
# get the pacf
plt.plot(pacf(df['diff12_1'][13:].values, method='ywm'))
plt.show()
# we infer that the season AR term is <= 1 and
# AR terms is <= 2 (all at standard threshold of 0.2)

# get acf
plt.plot(acf(df['diff12_1'][13:].values))
plt.show()
# we infer that season MA term <= 1 and
# MA terms <= 1 (all at standard threhold of 0.2)

# build the model (0,1,1, 0,1,1)12
model = SARIMAX(df['USAccDeaths'].values, order=(0,1,1), 
                 seasonal_order=(0,1,1,12), simple_differencing=True)
# simple differencing should be true so that the model is built after
# differencing and initial observations are discarded
res = model.fit()
print(res.summary())
"""
<class 'statsmodels.iolib.summary.Summary'>
                                     SARIMAX Results
==========================================================================================
Dep. Variable:                           D.DS12.y   No. Observations:                   59
Model:             SARIMAX(0, 0, 1)x(0, 0, 1, 12)   Log Likelihood                -425.441
Date:                            Sun, 14 Jun 2020   AIC                            856.882
Time:                                    10:23:01   BIC                            863.115
Sample:                                         0   HQIC                           859.315
                                             - 59
Covariance Type:                              opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
ma.L1         -0.4303      0.115     -3.748      0.000      -0.655      -0.205
ma.S.L12      -0.5527      0.181     -3.053      0.002      -0.908      -0.198
sigma2      9.935e+04   1.79e+04      5.560      0.000    6.43e+04    1.34e+05
===================================================================================
Ljung-Box (Q):                       31.42   Jarque-Bera (JB):                 1.63
Prob(Q):                              0.83   Prob(JB):                         0.44
Heteroskedasticity (H):               0.53   Skew:                             0.40
Prob(H) (two-sided):                  0.17   Kurtosis:                         2.91
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
"""
# thus the model becomes (we only have MA terms)
# (1-B)(1-B^12)X(t) = (1 - 0.4303 * B)(1 - 0.5527 * B^12)Z(t)
# where Z(t) is N(0, 99350)

# note that the no of observations used in building the model are 59
# instead of 72 because the initial few terms are ignored due to
# the seasonal and normal differencing

# get qqplot
qqplot(res.resid, line='q')
plt.show()

# get acf of resid
# we see no significant correlations at threshold of 0.2
plt.plot(acf(res.resid))
plt.show()

# get the Ljung-Box statistic p-values
# it returns two arrays, first is statistic, second is p-values
print(acorr_ljungbox(res.resid)[1])
# all p-values are much higher than 0.05 significance level
# the p-values correspond to different lags, hence there is no
# correlation till high number of lags and residuals are all white noise

# we can check the coefficient significance from the p-values in res.summary()

# since we set simple_differencing=True while training the model
# the predictions are the differenced values. Also, we have done differencing
# two times, once for seasonal trend and then single differencing for remaining trend

# note that the prediction is relative to index of training data
# and our training data is already after removing the first 13 observations
# due to differencing, we need to account for that
# pred(i-13) = (v(i) - v(i-12) - (v(i-1) - v(i-1-12))
# where v(i) is the actual value, i is relative to indices in df
# pred(i-13) has i-13 to account for fact that first 13 observations were
# not used in the model
# make the predictions, we use for loop since predictions into three months
# ahead are needed, and due to differencing, we will need to calculate intermediate
# values as well
# prepare the full series of correct length
pred_series = np.zeros(df.shape[0] + 3)
pred_series[:72] = df['USAccDeaths'].values

for i in range(72,75):
    pred_series[i] = res.predict(i-13) + pred_series[i-1]\
                        + pred_series[i-12] - pred_series[i-13]

print(pred_series[74])