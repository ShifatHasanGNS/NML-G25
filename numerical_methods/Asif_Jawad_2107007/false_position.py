import numpy as np


def false_position_method(coeffs, a, b, tolerance):
    fa = np.polyval(coeffs, a)
    fb = np.polyval(coeffs, b)

    if fa * fb >= 0:
        print("The function must have opposite signs at a and b for the false position method to work.")
        return np.nan

    while abs(b - a) >= tolerance:
        c = (a * fb - b * fa) / (fb - fa)
        fc = np.polyval(coeffs, c)

        if abs(fc) < tolerance:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c


def solve_using_false_position_method():
    degree = int(input("Enter the degree of the polynomial: "))

    coeffs = []
    print("Enter the coefficients (from highest degree to constant term):")
    coeffs = input().split()[:degree + 1]
    coeffs = [float(x) for x in coeffs]

    a = float(input("Enter the interval [a, b] to search for roots:\na = "))
    b = float(input("b = "))
    tolerance = 1e-7
    step = 0.01

    roots = []
    i = a
    while i < b:
        f_i = np.polyval(coeffs, i)
        f_next = np.polyval(coeffs, i + step)

        if f_i * f_next < 0:
            root = false_position_method(coeffs, i, i + step, tolerance)
            if not np.isnan(root):
                roots.append(root)

        i += step

    if roots:
        print(f"Roots found in the interval [{a}, {b}]:")
        for root in roots:
            print(f"{root:.6f}")

        if len(roots) < degree:
            print(
                f"\nWarning: Not all roots were found in the interval [{a}, {b}].")
            print(
                "There might be more roots outside this interval, or consider increasing the range.")
    else:
        print("No roots found in the given interval.")
