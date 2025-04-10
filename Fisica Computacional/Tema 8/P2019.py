import numpy as np
import matplotlib.pyplot as plt

tau=365
A=10
B=12
D=0.1

# Parte espacial
L=20
N=300
xp=np.linspace(0,L,N)
a=L/N

# Parte temporal
h=0.1
tp=np.arange(0,10*365+h,h)

# Conds. de contorno
T = np.zeros(N, float)
T[-1]=11 # a 20m bajo tierra tenemos T=11ºC = cte.

# Resolución: FTCS

times = 9*365*(1 + np.array([0,0.25,0.5,0.75,1]))

for t in tp:
    # Cond. inicial (dependiente del tiempo)
    T[0]=A+B*np.sin(2*np.pi*t/tau)
    T[1:N-1]+=h*D/a**2 * ( T[2:N]-2*T[1:N-1]+T[0:N-2] )
    for i in times:
        if np.abs(t-i)<h/10:
            plt.plot(xp, T, label=f"Mes {np.where(times==i)[0][0]}")
            plt.legend()

plt.show()
