# Para optimizar el algoritmo de la eliminación Gaussiana, tengo que saltarme las filas en las que haya pivote 0

import numpy as np

def tridiagonal(A, B):
    N = len(B)
    for i in range(N-1): # Solo tengo que ir hasta la penúltima fila porque en la última solo voy a dividir
        # Asumo que el primer elemento es 1 aunque no lo sea
        
        # Divido la fila por el pivote
        div = A[i,i]
        A[i,i+1] /= div
        B[i] /= div
        
        # Asumo que el término de abajo es 0 porque total ya lo voy a eliminar, así me ahorro 1 op
        # Resto la fila a la de abajo
        mult = A[i+1,i]
        A[i+1,i+1] -= A[i,i+1]*mult
        B[i+1] -= B[i]*mult
        
    # Última fila
    B[N-1] /= A[N-1,N-1]
    
    # Doy la solución
    x = np.empty(N, float)
    x[N-1] = B[N-1]
    for i in range(N-2, -1, -1): # Fíjate en que los elementos de la diagonal de A nunca aparecen --> por eso asumo que son 1
        x[i] = B[i]- A[i,i+1]*x[i+1]
    
    return x

N = 30
A = np.zeros((N,N), float)

k = 5
m = 1
w = 2
a = 2*k-m*w**2
C = 1

for i in range(1, N-1):
    A[i,i] = a
    A[i,i-1] = -k
    A[i,i+1] = -k


A[0,0] = a-k
A[0,1]=-k
A[-1,-1] = a-k
A[-1,-2] = -k

B = np.zeros(N)
B[0] = C

x = tridiagonal(A, B)
print(x)