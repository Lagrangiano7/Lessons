import numpy as np
import matplotlib.pyplot as plt

f = lambda x, t: -x**3+np.sin(t)
a=0
b=10

N=100
h=(b-a)/N

tp = np.linspace(a, b, N)
x=0

xp = []

for t in tp:
    xp.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+k1/2,t+h/2)
    
    x += k2


plt.plot(tp, xp)
plt.show()