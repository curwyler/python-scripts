# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 00:59:53 2017

@author: Cedar
"""
import csv
import numpy as np
import scipy as sc
import math
import matplotlib.pylab as plt

savepath = r'C:\Users\Cedar\polybox\Anderes\RPG\Shadowrun\Wahrscheinlichkeit'
#%%
"""
n   : number of dices
S   : number of successes
"""

def f(n,x):
    return sc.special.binom(n,x)*sc.power(5,n-x)

def f_crit(n,x):
    return sc.special.binom(n,x)*sc.power(3,n-x)

vf=np.vectorize(f)
vf_crit=np.vectorize(f_crit)
    
def prob_glitch(n):
    return sum( vf(n,  range(int(math.ceil((n+1)/2.)),n+1) )) /np.power(6,n)

def crit_glitch(n):
    return sum(vf_crit(n,  range(int(math.ceil((n+1)/2.)),n+1))) /np.power(6,n)
    
#for i in range(1,10):
#    print i, prob_glitch(i), crit_glitch(i)

#%% Probability
def prob(S, n):
    return sc.special.binom(n,S)* np.power(2./6.,S) * np.power(4./6., n-S)


plt.figure('Probability')
for n in range(2, 21, 4):
    S= [i for i in range(1,n+2)]
    S=np.array(S)
    plt.plot(prob(S,n), label=u'%i Würfel' %n, ls='--', marker='o')
plt.xlabel("Anzahl Erfolge")
ax = plt.gca()
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.0f}%'.format(x*100) for x in vals])
plt.legend()
plt.savefig(savepath+r'\Wahrscheinlichkeit.png')


def atleast(S,n):
    """
    Probability to have at least S successes with n dice
    """    
    S_greater = np.array([i for i in range(S,n+1)])
    return np.sum( prob(S_greater,n) )

atleast = np.vectorize(atleast)


plt.figure('atleast')
for n in range(2, 21, 4):
    S= [i for i in range(1,n+2)]
    S=np.array(S)
    plt.plot(atleast(S,n), label=u'%i Würfel' %n, ls='--', marker='o')
plt.xlabel("Anzahl Erfolge")
#plt.ylabel("Wahrscheinlichkeit")
ax = plt.gca()
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.0f}%'.format(x*100) for x in vals])
plt.legend()
plt.savefig(savepath+r'\Wahrscheinlichkeit mindestens.png')


with open(savepath+r'\prob.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    S=np.arange(10)
    for n in range(1, 21):
        writer.writerow(['%.1f' %k for k in prob(S,n)*100])
        
with open(savepath+r'\atleast.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    S=np.arange(10)
    for n in range(1, 21):
        writer.writerow(['%.1f' %k for k in atleast(S,n)+100])
        