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

df = pd.read_csv('data\shot_logs_pos.csv')
df_features = df[['GAME_ID','MATCHUP','FGM','PTS_TYPE','CLOSE_DEF_DIST','player_name','player_pos', 'player_pos_ID','CLOSEST_DEFENDER' ,'CD_pos',
       'CD_pos_ID']]
	   
df_features.reset_index(drop=True,inplace=True)
df_PG = df_features[df_features['player_pos']=='PG']
df_PG['miss match'] = df_PG['CD_pos_ID'].apply(attack_mm_PG)
print(df_PG.head())

df_C = df_features[df_features['player_pos']=='C']
df_C['miss match'] = df_C['CD_pos_ID'].apply(attack_mm_C)
print(df_C.head())

#fig = plt.figure(figsize=(12,6))
#sns.set_style('whitegrid')
#sns.distplot(df_features[df_features['PTS_TYPE']==2]['CLOSE_DEF_DIST'],kde=False,bins=50)
#sns.distplot(df_features[df_features['PTS_TYPE']==3]['CLOSE_DEF_DIST'],kde=False,bins=50)
#plt.savefig(fig, dpi=600,)