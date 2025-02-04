import re
import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def evaluate_expression(expression):
    """Evaluates a mathematical expression following BODMA rules."""
    try:
        return eval(expression, {"__builtins__": None}, OPS)
    except Exception as e:
        return f"Error: {str(e)}"

def validate_expression(expression):
    """Validates if an expression contains only allowed characters."""
    pattern = r'^[0-9+\-*/^(). ]+$'
    if not re.match(pattern, expression):
        raise ValueError("Invalid characters in expression")
    return True
