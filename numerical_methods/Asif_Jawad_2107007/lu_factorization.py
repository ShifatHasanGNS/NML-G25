import numpy as np


def solve_using_lu_factorization_method():
    try:
        n = int(input("Enter the number of linear equations for the system: "))
        if n <= 0:
            raise ValueError(
                "The number of equations must be a positive integer.")

        A = np.zeros((n, n))  # Coefficient Matrix
        L = np.zeros((n, n))  # Lower Triangular Matrix
        U = np.zeros((n, n))  # Upper Triangular Matrix
        P = np.eye(n)         # Permutation matrix
        b = np.zeros(n)       # Constant Vector
        x = np.zeros(n)       # Solution Vector
        y = np.zeros(n)       # Intermediate Vector

        # Input coefficient matrix A
        print(f"\nEnter the {n}x{n} coefficient matrix (A):")
        for i in range(n):
            values = input().split()
            if len(values) != n:
                raise ValueError(f"Expected {n} values for row {i + 1}.")
            A[i] = [float(x) for x in values]

        # Input right-hand side vector b
        print("\nEnter the right-hand side constant vector (b):")
        values = input().split()
        if len(values) != n:
            raise ValueError(f"Expected {n} values for vector b.")
        b = np.array([float(x) for x in values])

        # Perform LU decomposition with partial pivoting
        for i in range(n):
            # Pivoting: Find the maximum element in the current column
            max_row = np.argmax(abs(A[i:, i])) + i
            if A[max_row, i] == 0:
                raise ValueError(
                    "Matrix is singular and cannot be decomposed.")

            # Swap rows in A and P for partial pivoting
            if max_row != i:
                A[[i, max_row]] = A[[max_row, i]]
                P[[i, max_row]] = P[[max_row, i]]
                if i > 0:
                    # Swap previous L values
                    L[[i, max_row], :i] = L[[max_row, i], :i]

            # Upper triangular matrix U
            for k in range(i, n):
                sum_upper = sum(L[i, j] * U[j, k] for j in range(i))
                U[i, k] = A[i, k] - sum_upper

            # Lower triangular matrix L
            for k in range(i, n):
                if i == k:
                    L[i, i] = 1
                else:
                    sum_lower = sum(L[k, j] * U[j, i] for j in range(i))
                    L[k, i] = (A[k, i] - sum_lower) / U[i, i]

        # Apply permutation matrix to b to get Pb
        Pb = np.dot(P, b)

        # Forward substitution to solve L * y = Pb
        for i in range(n):
            sum_y = sum(L[i, j] * y[j] for j in range(i))
            y[i] = Pb[i] - sum_y

        # Backward substitution to solve U * x = y
        for i in range(n - 1, -1, -1):
            sum_x = sum(U[i, j] * x[j] for j in range(i + 1, n))
            if U[i, i] == 0:
                raise ValueError(
                    "Division by zero during back substitution. Matrix may be singular.")
            x[i] = (y[i] - sum_x) / U[i, i]

        print("\nSolution (x values):")
        for i in range(n):
            print(f"x{i + 1} = {x[i]:.6f}")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
