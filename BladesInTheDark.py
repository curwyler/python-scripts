# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 10:03:28 2017

@author: Cedar

Blades in the Dark Probabilities
"""

import numpy as np
import pandas as pd

def prob(n):
    """
    Returns the probabilities to get a 6, a 4 or 5 and a 1,2 or 3.
    """
    p6 = 1. - (5./6.)**n
    p123 = 0.5**n
    p45 = 1-p6-p123
    return [p123,p45,p6]

saveto = r'C:\Users\Cedar\polybox\RPG\Blades in the Dark'
k=8

other = [prob(i+1) for i in range(k)]
index = [str(i+1)+'d6' for i in range(k)]
columns = ['1,2,3', '4,5', '6']

Table = pd.DataFrame(other, index=index, columns=columns)
print(Table)
Table.to_csv(saveto+r'\probabilities.csv')