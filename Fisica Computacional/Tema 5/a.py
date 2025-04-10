import numpy as np

def eigvals_Jacobi(A, tol):
    N = len(A)
    mask = ~np.eye(A.shape[0],dtype=bool) # Selecciona todos los elementos fuera de la diagonal
    err = 1.0
    while err > tol:
        A_mask = np.abs(A[mask])
        ind_max = np.where(A_mask == np.max(A_mask))[0][0]
        p, q = (ind_max%N, ind_max//N)
        
        # Ahora calculamos el ángulo de rotación
        theta = 1/2*np.arctan(2*A[p,q]/(A[p,p]-A[q,q]))
        c = np.cos(theta)
        s = np.sin(theta)
        R = np.eye(N, float)
        R[p,p]=c
        R[q,q]=s
        R[p,q]=-s
        R[q,p]=s



A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], float)

eigvals_Jacobi(A, 0.1)