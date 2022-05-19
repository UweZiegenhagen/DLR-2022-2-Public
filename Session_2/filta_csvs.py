# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:56:38 2022

@author: Uwe
"""

import pandas as pd

df = pd.read_csv('Beispiel.csv',sep=';')
print(df)

df = df[df['Betrag']>10]
print('\n',df)

df.to_latex('ergebnis.tex')
