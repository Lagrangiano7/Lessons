import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

t = np.linspace(0,100,1000)
V,P = np.meshgrid(t, t)

def T(V, P):
    return P*V

ax.plot_surface(V, P, T(V, P), cmap="hot")
ax.set_xlabel("V")
ax.set_ylabel("P")
ax.set_zlabel("T")
plt.show()

"""t = np.linspace(0,100,10000)

V, P = np.meshgrid(t, t)

T = P*V

plt.imshow(T, origin="lower", cmap="hot", extent=[0,100,0,100])
plt.colorbar()
plt.show()"""