import numpy as np
from numpy._typing._array_like import NDArray

MAX_ITERATIONS = 100
TOLERANCE = 1e-6


def make_diagonally_dominant(A):
    n = A.shape[0]
    for i in range(n):
        # Swap rows if the diagonal element is not dominant
        if abs(A[i][i]) <= sum(abs(A[i][j]) for j in range(n) if j != i):
            # Try to find a row below i to swap with for dominance
            for k in range(i + 1, n):
                if abs(A[k][i]) > abs(A[i][i]):
                    A[[i, k]] = A[[k, i]]  # Swap rows
                    break

    # Check if matrix is now strictly diagonally dominant
    for i in range(n):
        if abs(A[i][i]) <= sum(abs(A[i][j]) for j in range(n) if j != i):
            print(
                "\nWarning:\n  The matrix is not strictly diagonally dominant and the result may not be correct.\n  So, please apply 'Gauss or Jordan Elimination Method' to solve the system.\n")
            return None
    return A


def gauss_seidel_method(augmented_matrix: np.ndarray):
    mat = make_diagonally_dominant(augmented_matrix)

    if mat is None:
        return
    else:
        augmented_matrix = mat

    coefficient_matrix = augmented_matrix[:, :-1]
    constant_vector = augmented_matrix[:, -1]

    num_vars = len(constant_vector)

    # Check if system is solvable
    if coefficient_matrix.shape[0] != num_vars or coefficient_matrix.shape[1] != num_vars:
        print("The system is not solvable.")
        return

    # Initial guesses for the variables
    x = np.zeros(num_vars)
    new_x = np.zeros(num_vars)

    for iteration in range(MAX_ITERATIONS):
        for i in range(num_vars):
            sum_except_i = np.sum(
                [coefficient_matrix[i, j] * x[j] for j in range(num_vars) if j != i])
            new_x[i] = (constant_vector[i] - sum_except_i) / \
                coefficient_matrix[i, i]

            if np.allclose(x, new_x, rtol=TOLERANCE):
                break

            x[i] = new_x[i]

    print(f"\nRoots: {x}\n")


def solve_using_gauss_seidel_method():
    n = int(input("Enter the number of linear-equations for your system: "))
    rows, cols = n, n + 1

    M = np.array([], dtype=float)

    print(f"\nEnter the {rows}x{cols} Augmented Matrix (A | b):")
    for i in range(rows):
        R = list(map(float, input().split()))
        M = np.append(M, R)

    M = M.reshape((rows, cols))

    gauss_seidel_method(M)
