import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('HistoricalQuotes.csv',index_col=0)
data=data.head(5)
data=data.dropna(axis=0, how='all')
print(data.head())
x = data[['open','close']]
y = data['high']
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1)
print(x_train)
print(x_test)
linreg = LinearRegression()
linreg.fit(x_train,y_train)

y_test = linreg.predict(x_test)
print(y_test)