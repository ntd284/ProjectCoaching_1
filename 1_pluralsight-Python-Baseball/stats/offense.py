import pandas as pd
import matplotlib.pyplot as plt
from data import games

games = games()
plays = games.loc[games['type'] == 'play']
plays = plays.rename(columns={'multi2':'inning',
                              'multi3':'team',
                              'multi4':'player',
                              'multi5':'count',
                              'multi6':'pitches'})
plays = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)',regex = True)]
hits = plays.loc[:,['inning','event']]
hits['inning'] = pd.to_numeric(hits.loc[:,'inning'])

replacement = {r'^S(.*)': 'single',
               r'^D(.*)': 'double',
               r'^T(.*)': 'triple',
               r'^HR(.*)': 'hr'}
hit_type = hits['event'].replace(replacement,regex=True)
hits = hits.assign(hit_type=hit_type)
hits = hits.groupby(['inning','hit_type']).size().reset_index(name='count')
hits['hit_type'] = pd.Categorical(hits['hit_type'],['single', 'double', 'triple','hr'], ordered = True)
hits = hits.sort_values(['inning','hit_type'])
hits = hits.pivot(index='inning',columns='hit_type',values='count')
hits.plot.bar(stacked=True)
plt.show()
