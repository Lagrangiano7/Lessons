import numpy as np

A = np.array([[1, 2, 3], [7, 5, 6], [7, 8, 9]], float)

col = A[:,0] # Primera columna

pivote = np.max(col)
ind = np.where(col==pivote)[0][0]

print(A)
print(ind, pivote)