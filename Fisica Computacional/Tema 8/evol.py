import numpy as np
import matplotlib.pyplot as plt
from banded import banded

L=2.0e-9
m = 9.109*1e-31
k = 5*1e10
hbar = 6.63*1e-34/(2*np.pi)
x0=L/2
sigma=1e-10
k=5*1e10

# Parte espacial
N=999
xp = np.linspace(0,L,N+1)
a = L/N

# Parte temporal
h=1e-18
tp = np.arange(0,1000*h,h)


a1 = 1+1j*h*hbar/(2*m*a**2)
a2 = -1j*h*hbar/(4*m*a**2)
b1 = 1-1j*h*hbar/(2*m*a**2)
b2 = 1j*h*hbar/(4*m*a**2)

A = np.empty((N+1,N+1), complex)

A[0,:] = a2
A[1,:] = a1
A[2,:] = a2

def solveEvol(t_max):
    t=0
    # Cond. inicial
    Psi = np.exp(-(xp-x0)**2/(2*sigma**2))*np.exp(1j*k*xp)
    Psi[0]=Psi[-1]=0
    while t < t_max:
        # Resuelvo el sistema Av(t+h)=Bv(t) para obtener evol. temporal
        b = Psi[1:N]*b1 + b2*Psi[2:N+1] + b2*Psi[0:N-1]
        Psi[1:N] = banded(A, b, 1, 1)
        t+=h
    return Psi

Psi = np.exp(-(xp-x0)**2/(2*sigma**2))*np.exp(1j*k*xp)
Psi[0]=Psi[-1]=0

res = Psi.copy()

for t in tp[1:]:
	b = Psi[1:N]*b1 + b2*Psi[2:N+1] + b2*Psi[0:N-1]
	Psi[1:N] = banded(A, b, 1, 1)
	res = np.vstack((res, np.real(Psi)))

ind = np.where(tp==400*h)[0][0]

# Animación

#importing libraries
import numpy as np
import time
import matplotlib.pyplot as plt

# to run GUI event loop
plt.ion()

# here we are creating sub plots
figure, ax = plt.subplots(figsize=(10, 8))
line1, = ax.plot(xp, res[0,:])

# setting title
plt.title("Geeks For Geeks", fontsize=20)

# setting x-axis label and y-axis label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Loop
for i in range(1, len(res)):
	# creating new Y values
	new_y = res[i,:]

	# updating data values
	line1.set_xdata(xp)
	line1.set_ydata(new_y)

	# drawing updated values
	figure.canvas.draw()

	# This will run the GUI event
	# loop until all UI events
	# currently waiting have been processed
	figure.canvas.flush_events()

	#time.sleep(0.00001)
	if i==ind:
		print(1)
		time.sleep(500)