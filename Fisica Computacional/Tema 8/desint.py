# Prob. de que NO se desintegre un átomo de Tl es 2^(-t/Tau)

import numpy as np
from random import random
import matplotlib.pyplot as plt

Tau = 3.053*60

N_Tl=1000 # atomos de Tl, inicialmente
N_Pb = 0
t_max=1e3
tp = np.linspace(0,t_max, 10**6)

p = lambda t: 1-2**(-t/Tau)

Tl=[]
Pb=[]

for t in tp:
    Tl.append(N_Tl)
    Pb.append(N_Pb)
    
    decay=0
    
    for i in range(N_Tl):
        if random() < p(t):
            decay+=1
    N_Tl-=decay
    N_Pb+=decay
    
plt.plot(tp, Tl, "r")
plt.plot(tp, Pb, "b")
plt.show()