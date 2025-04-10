import numpy as np
import matplotlib.pyplot as plt

r=1.2
x = 0.1
xp=[]

for i in range(20):
    xp.append(x)
    x = r*x*(1-x)

plt.plot(xp, "ro")
plt.show()