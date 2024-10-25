import numpy as np
import sympy as sp
from sympy import symbols, sympify
from sympy import exp, log, sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, asinh, acosh, atanh
import numerical_methods as nm


def is_transcendental(equation_str: str):
    try:
        x = symbols('x')
        expr = sympify(equation_str)

        transcendental_funcs = {exp, log, sin, cos, tan, sinh,
                                cosh, tanh, asin, acos, atan, asinh, acosh, atanh}

        for func in transcendental_funcs:
            if expr.has(func):
                return True

        return False

    except Exception as e:
        print("Error in parsing the equation:", e)
        return None


def evaluate_equation(equation_str: str, x_val: float) -> float:
    try:
        x = symbols('x')
        expr = sympify(equation_str)
        result = float(expr.subs(x, x_val))
        print(result)
        return result
    except Exception as e:
        print("Error in parsing the equation:", e)
        return None


def parse_coefficients(polynomial_expr: str):
    x = sp.symbols('x')
    poly = sp.sympify(polynomial_expr)
    coefficients = sp.Poly(poly, x).all_coeffs()
    coefficients = [float(c) for c in coefficients]
    return list(coefficients)


def cauchys_bound(polynomial_expr: str):
    coeffs = parse_coefficients(polynomial_expr)
    number_of_roots = len(coeffs) - 1
    max_coeff = np.max(np.abs(coeffs[1:]))
    cauchys_bound_value: float = 1 + max_coeff / np.abs(coeffs[0])
    return -cauchys_bound_value, cauchys_bound_value, number_of_roots


def initial_bound_for_single_root(equation_str: str, x_min: float, x_max: float):
    step_size = np.abs(x_max - x_min) / nm.STEPS

    a = x_min
    b = a + step_size

    A, B = nm.evaluate_equation(
        equation_str, a), nm.evaluate_equation(equation_str, b)

    it_count = 0

    while A * B > 0 and b <= x_max and it_count < nm.MAX_ITERATIONS:
        a += step_size
        b += step_size
        A, B = nm.evaluate_equation(
            equation_str, a), nm.evaluate_equation(equation_str, b)

        it_count += 1

    return np.clip(a, x_min, x_max), np.clip(b, x_min, x_max)
