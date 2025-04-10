from simpson import simpson
import numpy as np
import matplotlib.pyplot as plt

def J(m, x):
    f = lambda t: np.cos(m*t-x*np.sin(t))
    I = 1/np.pi*simpson(f, 0,np.pi,1000)
    return I

