import numpy as np 
import pandas as pd 

header_1Nf = ['NA','NA','NA','NA', 
            'NA', '87', '88', 'NA', 
            'NA', '97', 'NA', '98']

header_f50Nf = ['77', '79', '80', '81', 
            '89', '90', '91', '92', 
            '99', '100', '1', '2']

header_100Nf = ['82', '83', '84', '85', 
            '93', '94', '95', '96', 
            '3', '5', '6', '7']

df_f = pd.read_csv('./force_data/20200423_force_performances.csv')
