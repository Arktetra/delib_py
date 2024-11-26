import math

def mul(x: float, y: float) -> float:
    """$f(x, y) = x * y$"""
    return x * y

def id(x: float) -> float:
    """$f(x) = x$"""
    return x

def add(x: float, y: float) -> float:
    """$f(x, y) = x + y$"""
    return x + y

def neg(x: float) -> float:
    """$f(x) = -x$"""
    return -x

def lt(x: float, y: float) -> float:
    """f(x, y) = 1.0 if x is less than y else 0.0"""
    return 1.0 if x < y else 0.0
    
def eq(x: float, y: float) -> float:
    """f(x, y) = 1.0 if x is equal to y else 0.0"""
    return 1.0 if x == y else 0.0

def max(x: float, y: float) -> float:
    """f(x, y) = x if x is greater than y else y"""
    return x if x > y else y

def is_close(x: float, y: float) -> bool:
    """f(x, y) = |x - y| < 1e-2"""
    return abs(x - y) < 1e-2

def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))
    
def relu(x: float) -> float:
    return x if x > 0 else 0

def relu_back(x: float, d: float) -> float:
    return d if x > 0 else 0

def log(x: float) -> float:
    assert x > 0., "x must be greater than 0."
    return math.log(x)

def log_back(x: float, d: float) -> float:
    assert x > 0., "x must be greater than 0."
    return d * 1 / x

def exp(x: float) -> float:
    return math.exp(x)

def inv(x: float) -> float:
    assert x != 0., "x must be a non-zero number."
    return 1 / x

def inv_back(x: float, d: float) -> float:
    return - d * 1 / x ** 2