from sympy import symbols, diff, integrate

def derivative(expression, variable):
    """Calculate the derivative of a mathematical expression."""
    x = symbols(variable)
    return diff(expression, x)

def integral(expression, variable):
    """Calculate the integral of a mathematical expression."""
    x = symbols(variable)
    return integrate(expression, x)