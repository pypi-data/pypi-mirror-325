def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Handles division by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def power(a, b):
    """Returns a raised to the power of b."""
    return a ** b
