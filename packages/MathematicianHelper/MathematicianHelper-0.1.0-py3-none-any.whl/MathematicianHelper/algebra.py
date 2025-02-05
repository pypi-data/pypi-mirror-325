import numpy as np
import math

def solve_quadratic(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)

def solve_linear_system(coefficients, constants):
    """Solve a system of linear equations using Gaussian elimination."""
    A = np.array(coefficients)
    B = np.array(constants)
    try:
        solution = np.linalg.solve(A, B)
        return solution.tolist()
    except np.linalg.LinAlgError:
        return None  # No unique solution