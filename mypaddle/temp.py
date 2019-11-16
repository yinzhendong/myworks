import numpy as np
from scipy import sparse


x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))

eye = np.eye(4)
print('NumPy array:\n', eye)

sparse_matrix = sparse.csr_matrix(eye)
print('\nSciPy sparse CSR matrix:\n', sparse_matrix)

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print('COO representation:\n',eye_coo)

import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker='x')
plt.show()
