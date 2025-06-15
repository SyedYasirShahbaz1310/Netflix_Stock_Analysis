import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


data = pd.read_csv("NFLX.csv")

# print(data)

# sns.set(rc={'figure.figsize' : (10,5)})
data['Date']= pd.to_datetime(data['Date'])
data = data.set_index('Date')
print(data)

# sns.lineplot(x = data.index, y = data['Volume'], label = 'Volume')
# plt.title("Volume of Sock VS Time")
# print(plt.show())

# data.plot(y = ['High', 'Close','Open'], title = 'Netplix stock price')
# print(plt.show())   

# fig, (ax1,ax2,ax3) = plt.subplots(3, figsize = (13,10))
# data.groupby(data.index.day).mean().plot(y = 'Volume', ax = ax1, xlabel = 'Day')
# data.groupby(data.index.month).mean().plot(y = 'Volume', ax = ax2, xlabel = 'Month')
# data.groupby(data.index.year).mean().plot(y = 'Volume', ax = ax3, xlabel = 'Year' , color = 'red')
# print(plt.show())

#toP-5 highest 5 years stock
# a = data.sort_values(by = 'High', ascending =  False).head(5)
# print(a['High'])


#toP-5 lowest 5 years stock

# a = data.sort_values(by = 'Low', ascending =  True).head(5)
# print(a['Low'])


# fig,axex = plt.subplots(nrows =1 ,ncols = 2, figsize = (12,5))
# fig.suptitle("High & Low Stocks Value Analysis ")
# sns.lineplot(ax = axex[0], y = data['High'], x = data.index, color = 'green')
# sns.lineplot(ax = axex[1], y = data['Low'], x = data.index, color = 'red')
# print(plt.show())