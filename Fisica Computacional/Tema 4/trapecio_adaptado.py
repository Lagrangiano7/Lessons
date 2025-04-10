import numpy as np

def trap_adapt(f, a, b, tol):
    N = 1 # Empezamos con un solo intervalo
    h = (b-a)/N
    I1 = h/2*(f(a)+f(b))
    err = 1
    cont = 1
    
    while err > tol: # Cogiendo err = 1 arbitrariamente (>tol) garantizo que por lo menos hago 1 iteración porque necesito 2 vals para calcular el error
        h/=2 # Duplico número de intervalos
        I2=0
        for k in range(N): # Es N en vez de N/2 porque estoy usando el viejo valor de N
            I2+=f(a+(2*k+1)*h)
        I2=I1/2+h*I2
        err = np.abs(I2-I1)/3
        I1=I2
        N*=2
        print(cont)
        cont+=1
    print(err)
    return I2

f = lambda x: np.sin(10*np.sqrt(x))**2
print(trap_adapt(f, 0, 1, 10**(-6)))