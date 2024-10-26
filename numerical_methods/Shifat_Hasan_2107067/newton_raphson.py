import numpy as np
import numerical_methods as nm

MAX_ITERATIONS = 1000
TOLERANCE = 1e-6


def newton_raphson(f: str, df: str, x0: float):
    try:
        x = x0
        for _ in range(MAX_ITERATIONS):
            x1 = x - (nm.evaluate(f, x) / nm.evaluate(df, x))
            if abs(x1 - x) < TOLERANCE:
                return x1
            x = x1
        return None

    except Exception as e:
        print("Error in newton_raphson:", e)
        return None


def solve_using_newton_raphson_method():
    try:
        f = input("\nEnter the function  :  ")
        df = input("Enter the derivative:  ")

        if not nm.is_transcendental(f):
            x_min, x_max, n_roots = nm.cauchys_bound(f)
            print(f"\nThe equation has {
                n_roots} roots and they are in the range: [{x_min}, {x_max}]\n")

        x0 = float(input("\nEnter a local-approximation for one of the roots:  "))
        root = newton_raphson(f, df, x0)
        if root is not None:
            print(f"\nRoot: {root}\n")
        else:
            print("\nRoot not found!\n")

        should_continue = input("\nDo you want to find more roots? (y/n):  ")

        while should_continue.lower() == 'y':
            x0 = float(
                input("\nEnter a local-approximation for one of the roots:  "))
            root = newton_raphson(f, df, x0)
            if root is not None:
                print(f"\nRoot: {root}\n")
            else:
                print("\nRoot not found!\n")

            should_continue = input(
                "\nDo you want to find more roots? (y/n):  ")

    except Exception as e:
        print("Error in solve_using_newton_raphson_method:", e)
        return None
