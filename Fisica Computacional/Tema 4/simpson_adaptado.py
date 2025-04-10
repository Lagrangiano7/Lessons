import numpy as np

def romberg(f, a, b, tol):
    # Calculo R11 y R22 y a partir de ahí aplico regla recursiva
    
    # Cálculo de R11
    h=b-a
    R11 = h/2*(f(a)+f(b))

    R1 = np.array([R11], float)
    err = 1.0
    n = 1

    while True:
        n+=1
        h/=2

        # Calculo el primer término y el resto los saco por recursión
        Rn1 = 1/2*(f(a)+f(b))
        for k in range(1,n):
            Rn1+=f(a+k*h)
        Rn1*=h

        R = np.empty(n,float)
        R[0]=Rn1

        for i in range(1,n):
            error = 1/(4**i-1)*(R[i-1]-R1[i-1])
            R[i]=R[i-1] + error
            if np.abs(error) < tol:
                return (R[i], np.abs(error), n*i)
        R1 = R
        

f = lambda x: np.sin(10*np.sqrt(x))**2
I, err, cont = romberg(f, 0,1,10**(-6))

print(I, err, cont)