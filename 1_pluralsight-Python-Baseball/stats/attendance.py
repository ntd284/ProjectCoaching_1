import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from data import games

games = games()
games = games.loc[(games['type'] == 'info')&(games['multi2'] == 'attendance')]
attendance = games.loc[:,['year','multi3']]
attendance.rename(columns={'multi3':'attendance'},inplace=True)
selection = attendance.loc[:,'attendance']
selection = pd.to_numeric(selection)
attendance['attendance'] = selection

attendance.plot(x='year', 
         y='attendance', 
         figsize=(15, 7),
         kind='bar')
plt.xlabel('x-axis') 
plt.ylabel('y-axis') 
mean = attendance['attendance'].mean()
plt.axhline( mean,
            label = 'x-axis',
            linestyle='dashed',
            color = 'green' )
plt.show()


