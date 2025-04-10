import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1+1/4*np.tanh(4*x)

N=100
xp = np.linspace(-1,1,N)
h = 10**(-8) # Minimizo error tomando este paso

# Adelantada
der1 = (f(xp+h)-f(xp))/h # Función vectorizada por ser de numpy, no es preciso un bucle

# Atrasada
der2 = (f(xp)-f(xp-h))/h

# Centrada
h = 10**(-5)
der3 = (f(xp+h/2)-f(xp-h/2))/h

der_teo = 1/np.cosh(4*xp)**2

plt.grid()
plt.plot(xp, der1, "ko")
plt.plot(xp, der2, "ro")
plt.plot(xp, der3, "bo")
plt.plot(xp, der_teo)
plt.show()