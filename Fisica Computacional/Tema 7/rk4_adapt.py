# Sin paso adaptado (paso fijo)
import numpy as np
import matplotlib.pyplot as plt

G=6.6743*10**(-11)
M = 1.989*10**(30)

fx = lambda vx: vx
fvx = lambda x, y: -G*M*x/(x**2+y**2)**1.5

fy = lambda vy: vy
fvy = lambda x, y: -G*M*y/(x**2+y**2)**1.5

def F(r):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    return np.array([fx(vx), fy(vy), fvx(x, y), fvy(x, y)])


# Conds. iniciales
x0 = 410*10**12
y0 = 0

xp = [x0]
yp = [y0]

r = np.array([410*10**12, 0,0,500], float)


# Ahora con paso adaptado

d = 1*10**3/(365.25*24*3600) # km/s

x0=410*10**12
vy0=500

r = np.array([x0,0,0,vy0], float)

t=0
t_max=32*10**14
N=10**5
h = (t_max-t)/N

while t < t_max:
    k1 = 2*h*F(r)
    k2 = 2*h*F(r+k1/2)
    k3 = 2*h*F(r+k2/2)
    k4 = 2*h*F(r+k3)
    
    r1 = r + 1/6*(k1+2*k2+2*k3+k4) # Primera estimación
    
    # Ahora doy 2 pasos de longitud h
    k1 = h*F(r)
    k2 = h*F(r+k1/2)
    k3 = h*F(r+k2/2)
    k4 = h*F(r+k3)
    
    r2 = r + 1/6*(k1+2*k2+2*k3+k4)
    
    k1 = h*F(r2)
    k2 = h*F(r2+k1/2)
    k3 = h*F(r2+k2/2)
    k4 = h*F(r2+k3)
    
    r2+= 1/6*(k1+2*k2+2*k3+k4) # Segunda estimación
    
    x_err = r1[0]-r2[0]
    y_err = r1[1]-r2[1]
    
    err = np.sqrt(x_err**2+y_err**2)
    
    p = 30*h*d/err
    
    # Si p > 1, el paso que hemos dado es válido porque h_obj > h pero no hace falta hacerlo tan pequeño
    if p>1:
        r=r2 # r solo se actualiza si logramos alcanzar la tolerancia o sobrepasarla
        t+=2*h
        h = np.min([p**(1/4)*h, 2*h])
        xp.append(r[0])
        yp.append(r[1]) # Metemos r2 porque es el más preciso, es el que hemos calculado con 2 pasos
    else:
        h*=p**(1/4)

plt.scatter(xp, yp)
plt.show()