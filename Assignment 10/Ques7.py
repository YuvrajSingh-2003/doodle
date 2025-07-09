import numpy as np
A = np.array([[1, -2, 3], [1, 3, -1], [2, -5, 5]])
B = np.array([9, -6, 17])

X = np.linalg.inv(A).dot(B)
print("Solution [x, y, z]:", X)