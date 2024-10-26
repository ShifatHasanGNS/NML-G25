import numpy as np
import sympy as sp
from sympy import exp, log, sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, asinh, acosh, atanh


# ---------------------------------------- #
# ---------- For : Shifat Hasan ---------- #

def is_transcendental(equation_str: str):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(equation_str)

        transcendental_funcs = {exp, log, sin, cos, tan, sinh,
                                cosh, tanh, asin, acos, atan, asinh, acosh, atanh}

        for func in transcendental_funcs:
            if expr.has(func):
                return True

        return False

    except Exception as e:
        print("Error in parsing the equation:", e)
        return None


def evaluate(equation_str: str, x_val: float) -> float:
    equation_str = equation_str.replace("^", "**")
    equation_str = equation_str.replace("e", "2.7182818285")
    equation_str = equation_str.replace("pi", "3.1415926536")
    try:
        x = sp.symbols('x')
        expr = sp.sympify(equation_str)
        result = float(expr.subs(x, x_val))
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
    polynomial_expr = polynomial_expr.replace("^", "**")
    polynomial_expr = polynomial_expr.replace("e", "2.7182818285")
    polynomial_expr = polynomial_expr.replace("pi", "3.1415926536")
    coeffs = parse_coefficients(polynomial_expr)
    number_of_roots = len(coeffs) - 1
    max_coeff = np.max(np.abs(coeffs[1:]))
    cauchys_bound_value: float = 1 + max_coeff / np.abs(coeffs[0])
    return -cauchys_bound_value, cauchys_bound_value, number_of_roots


# ------------------------------------- #
# ---------- For : Ankon Roy ---------- #

def take_func_rk():
    math_function_mapping = {
        'sin': 'np.sin',
        'cos': 'np.cos',
        'tan': 'np.tan',
        'exp': 'np.exp',
        'log': 'np.log',
        'sqrt': 'np.sqrt',
        'pi': 'np.pi',
        'e': 'np.e',
        '^': '**'
    }

    function_input = input(
        "Enter a function of x and y (use 'x' and 'y' as variables) dy/dx = ")

    for func in math_function_mapping:
        function_input = function_input.replace(
            func, math_function_mapping[func])

    return lambda x, y: eval(function_input, {"x": x, "y": y, "np": np})
