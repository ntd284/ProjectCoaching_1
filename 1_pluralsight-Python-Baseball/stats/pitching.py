import pandas as pd
import matplotlib.pyplot as plt
from data import games
games = games()
plays = games[games['type'] == 'play']
strike_outs = plays[plays['event'].str.contains('K')]
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
strike_outs = strike_outs.reset_index(name='strike_outs') 
strike_outs = strike_outs.loc[:,['year','strike_outs']].apply(pd.to_numeric)
plt.scatter(x=strike_outs['year'],
         y=strike_outs['strike_outs'])
plt.legend(['Strike Outs'])
plt.show()
# print(strike_outs.head(30))