def gauss_seidel():
    print("""

#This is program of Gauss-Siedel-method [prog - 11]

import numpy as np

# Define functions for iteration
f1 = lambda x, y, z: (17 - y + 2 * z) / 20
f2 = lambda x, y, z: (-18 - 3 * x + z) / 20
f3 = lambda x, y, z: (25 - 2 * x + 3 * y) / 20

# Initialize values
x0, y0, z0 = 0, 0, 0
count = 1

# User input: tolerable error
e = float(input("Enter tolerable error: "))

# Print table header
print(f"{'Count':<6} {'x':<10} {'y':<10} {'z':<10}")

# Gauss-Seidel Iteration
while True:
    # Correct order of updates
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)  # Use updated x1
    z1 = f3(x1, y1, z0)  # Use updated x1 and y1

    # Print iteration results
    print(f"{count:<6} {x1:<10.4f} {y1:<10.4f} {z1:<10.4f}")

    # Compute errors
    e1, e2, e3 = abs(x1 - x0), abs(y1 - y0), abs(z1 - z0)

    # Update values
    x0, y0, z0 = x1, y1, z1
    count += 1

    # Stop when all errors are within tolerance
    if e1 <= e and e2 <= e and e3 <= e:
        break

# Print final result
print(f"\nSolution: x = {x1:.3f}, y = {y1:.3f}, z = {z1:.3f}")

    
    
    
    """)