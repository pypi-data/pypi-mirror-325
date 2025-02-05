def eigenvalue_eigenvector():
    print("""
    
#This is program of Eigenvalues and Eigenvectors [prog - 12]

import numpy as np

# Define the matrix
I = np.array([[1, -3, 3],
              [3, -5, 3],
              [6, -6, 4]])

# Print the matrix
print(f"Given matrix:\n{I}")

# Compute eigenvalues and eigenvectors
w, v = np.linalg.eig(I)

# Print the eigenvalues
print(f"Eigenvalues:\n{w}")

# Print the eigenvectors
print(f"Eigenvectors:\n{v}")

    
    """)