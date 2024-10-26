import numerical_methods as nm

MAX_ITERATION = 21
TOLERANCE = 1e-6


def solve_using_secant_method():
    try:
        f = input("Enter a function of x (use 'x') = ")
        x0 = float(input("\nEnter a local-approximation for one of the roots:  "))

        a, b = x0 - 0.5, x0 + 0.5

        fb = nm.evaluate(f, b)

        for i in range(0, MAX_ITERATION):
            if abs(fb) < TOLERANCE:
                print(f"\nRoot: {b}\n")
                return

            fa, fb = nm.evaluate(f, a), nm.evaluate(f, b)

            c = b - fb * ((b - a) / (fb - fa))

            a = b
            b = c

        print("\nRoots not found in the given interval.\n")

    except Exception as e:
        print(f"Error: {e}")
        pass
