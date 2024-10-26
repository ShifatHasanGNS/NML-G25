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

        print(f"\nSuggestion:")
        print("  Keep Patience! We can find one root at a time...")

        roots = set()
        n_roots = 1

        if not nm.is_transcendental(f):
            x_min, x_max, n_roots = nm.cauchys_bound(f)
            print(f"  The equation has {
                  n_roots} roots and they are in the range: [{x_min}, {x_max}]")
            print(f"  It works only for Real-Number Roots. So, Be Careful!")
        else:
            print("  The equation is Transcendental, so it may have multiple roots.")
            n_roots = int(
                input("\nHow many roots do you want to find? (default: 1):  ") or 1)

        while len(roots) < n_roots:
            x0 = float(
                input("\nEnter a local-approximation for one of the roots:  "))
            root = newton_raphson(f, df, x0)
            if root is not None:
                print(f"\nRoot found: {root}")
                roots.add(root)
            else:
                print("\nRoot not found! Try again.\n")

        print(f"\n\nRoots: {list(roots)}\n")

    except Exception as e:
        print("Error in solve_using_newton_raphson_method:", e)
        return None
