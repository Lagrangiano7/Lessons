# Polinomio interpolador de Lagrange

import matplotlib.pyplot as plt
import numpy as np

# x_: eje X
# x: puntos seleccionados para interpolar
# coefs: representarn f(x_i)

def L(x_, x, coefs) -> np.array:
    N=x.size
    prod=np.ones_like(x_)
    s = np.zeros_like(x_)
    
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            prod*=(x_-x[j])/(x[i]-x[j])
        s+=coefs[i]*prod
        prod = np.ones_like(x_)
    return s

f = lambda x: np.sin(x)
x = np.linspace(-7,7,1000)
x_i = np.linspace(-5,5,2)
coefs = f(x_i)

pol = L(x, x_i, coefs)

plt.grid()
plt.plot(x, f(x), "b-")
plt.plot(x_i, f(x_i), "ro")
plt.plot(x, pol, "k--")
plt.show()

# Si quieres extrapolar la curva de interpolación, basta con que le des un eje x_ diferente a L

f = lambda x: 1/(1+25*x**2)
x = np.linspace(-3,3,1000)
x_i = np.linspace(-3,3,5)
coefs = f(x_i)
x_ = np.linspace(-4,4,1000)

plt.plot(x, f(x), "b-")
plt.plot(x_i, coefs, "ro")
plt.plot(x_, L(x_, x_i, coefs), "k--")
plt.show()