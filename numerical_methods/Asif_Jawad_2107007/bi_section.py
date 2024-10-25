import numpy as np


def bisection_method(coeffs, a, b, tolerance):
    while (b - a) >= tolerance:
        mid = (a + b) / 2
        f_a = np.polyval(coeffs, a)
        f_mid = np.polyval(coeffs, mid)

        if abs(f_mid) < tolerance:
            return mid

        if f_a * f_mid < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2


def solve_using_bisection_method():
    degree = int(input("Enter the degree of the polynomial: "))

    coeffs = []
    print("Enter the coefficients (from highest degree to constant term):")
    coeffs = input().split()[:degree + 1]
    coeffs = [float(x) for x in coeffs]

    coeffs = np.array(coeffs)

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
            root = bisection_method(coeffs, i, i + step, tolerance)
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
