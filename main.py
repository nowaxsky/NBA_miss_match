'''
Jan 14, 2017
CPM
NBA_shot_logs

Add player position information.

https://www.kaggle.com/dansbecker/nba-shot-logs
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model.miss_match import attack_mm_PG,attack_mm_C,attack_mm_SG,attack_mm_PF

df = pd.read_csv('data/shot_logs_pos.csv')
df_features = df[['GAME_ID','MATCHUP','W','FGM','PTS_TYPE','CLOSE_DEF_DIST',
				'player_name','player_pos', 'player_pos_ID','CLOSEST_DEFENDER' ,'CD_pos',
				'CD_pos_ID']]
	   
df_features.reset_index(drop=True,inplace=True)

df_PG = df_features.copy()
df_C = df_features.copy()
df_SG = df_features.copy()
df_PF = df_features.copy()

player_p = ['PG','C','SG','PF']
methods = [attack_mm_PG,attack_mm_C,attack_mm_SG,attack_mm_PF]
dataframes = [df_PF,df_C,df_SG,df_PF]

acc = []
for position,dataframe,method in zip(player_p,dataframes, methods):
    dftemp = dataframe[dataframe['player_pos'] == position]
    dftemp['miss match'] = dftemp['CD_pos_ID'].apply(method)
    acc.append(dftemp)

player_PG = acc[0].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])
player_C = acc[1].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])
player_SG = acc[2].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])
player_PF = acc[3].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])

dfout = pd.concat([player_PG,player_SG,player_PF,player_C],axis=1)
dfout.to_csv('output/dataframe_1.csv')
print(dfout)
heatmap = sns.heatmap(pd.concat([player_PG,player_SG,player_PF,player_C],axis=1),annot=True)
fig = heatmap.get_figure()
fig.savefig('output/figure_1.png')

player_PG = acc[0].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'],aggfunc='count')
player_C = acc[1].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'],aggfunc='count')
player_SG = acc[2].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'],aggfunc='count')
player_PF = acc[3].pivot_table(values='FGM',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'],aggfunc='count')

dfout = pd.concat([player_PG,player_SG,player_PF,player_C],axis=1)
dfout.to_csv('output/dataframe_2.csv')
print(dfout)
heatmap = sns.heatmap(pd.concat([player_PG,player_SG,player_PF,player_C],axis=1),annot=True)
fig = heatmap.get_figure()
fig.savefig('output/figure_2.png')

player_PG = acc[0].pivot_table(values='CLOSE_DEF_DIST',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])
player_C = acc[1].pivot_table(values='CLOSE_DEF_DIST',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])
player_SG = acc[2].pivot_table(values='CLOSE_DEF_DIST',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])
player_PF = acc[3].pivot_table(values='CLOSE_DEF_DIST',index=['miss match', 'PTS_TYPE'],columns=['player_pos_ID'])

dfout = pd.concat([player_PG,player_SG,player_PF,player_C],axis=1)
dfout.to_csv('output/dataframe_3.csv')
print(dfout)
heatmap = sns.heatmap(pd.concat([player_PG,player_SG,player_PF,player_C],axis=1),annot=True)
fig = heatmap.get_figure()
fig.savefig('output/figure_3.png')
