def fibonacci(n):
    """Generate the Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def newton_raphson(func, derivative_func, initial_guess, tolerance=1e-6, max_iterations=100):
    """Find the root of a function using the Newton-Raphson method."""
    x = initial_guess
    for _ in range(max_iterations):
        fx = func(x)
        if abs(fx) < tolerance:
            return x
        dfx = derivative_func(x)
        if dfx == 0:
            break  # Avoid division by zero
        x = x - fx / dfx
    return None  # No convergence