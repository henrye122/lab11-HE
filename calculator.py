# GitHub URL: https://github.com/henrye122/lab11-HE.git
# Partner 1: Henry Edinger

import math


def square_root(a):
    """Return the real square root of a; reject negative inputs."""
    try:
        return math.sqrt(a)
    except ValueError as error:
        raise ValueError("The square root argument must be nonnegative.") from error
    except TypeError as error:
        raise TypeError("The square root argument must be a real number.") from error


def hypotenuse(a, b):
    """Return the hypotenuse for two legs, allowing negative inputs."""
    try:
        return math.hypot(a, b)
    except TypeError as error:
        raise TypeError("Hypotenuse arguments must be real numbers.") from error


def add(a, b):
    """Return a plus b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def mul(a, b):
    """Return a multiplied by b."""
    return a * b


def div(a, b):
    """Return b divided by a; raise ZeroDivisionError when a is zero."""
    if a == 0:
        raise ZeroDivisionError("The divisor (first argument) cannot be zero.")
    return b / a


def logarithm(a, b):
    """Return log base a of b; raise ValueError for an invalid domain."""
    if a <= 0 or a == 1:
        raise ValueError("The logarithm base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("The logarithm argument must be positive.")
    return math.log(b, a)


def exp(a, b):
    """Return a raised to the power b."""
    return a ** b

