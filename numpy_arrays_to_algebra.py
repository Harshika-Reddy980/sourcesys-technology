import numpy as np

print("NUMPY ARRAYS")

# 1D array
a = np.array([1,2,3,4])
print("1D Array:", a)

# 2D array
b = np.array([[1,2],[3,4]])
print("2D Array:\n", b)


print("\nARRAY OPERATIONS")

x = np.array([10,20,30])
y = np.array([1,2,3])

print("Addition:", x+y)
print("Subtraction:", x-y)
print("Multiplication:", x*y)


print("\nMATRIX OPERATIONS")

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("Matrix A:\n",A)
print("Matrix B:\n",B)

print("Matrix Multiplication:\n", A @ B)


print("\nLINEAR ALGEBRA")

# determinant
print("Determinant:", np.linalg.det(A))

# inverse
print("Inverse:\n", np.linalg.inv(A))

# eigenvalues
values, vectors = np.linalg.eig(A)
print("Eigenvalues:", values)