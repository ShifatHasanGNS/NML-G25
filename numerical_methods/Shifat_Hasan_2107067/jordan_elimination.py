import numpy as np


def row_echelon(Augmented_Matrix: np.ndarray) -> np.ndarray:
    M = Augmented_Matrix.copy()
    rows, cols = M.shape

    for i in range(min(rows, cols)):
        if M[i, i] == 0:
            for j in range(i+1, rows):
                if M[j, i] != 0:
                    M[[i, j]] = M[[j, i]]
                    break

        if M[i, i] == 0:
            continue

        for j in range(i+1, rows):
            M[j] = M[i, i]*M[j] - M[j, i]*M[i]

    return M


def jordan(Augmented_Matrix: np.ndarray) -> tuple[np.ndarray, list[float]]:
    M = row_echelon(Augmented_Matrix)
    n, _ = M.shape

    for i in range(n-1, 0, -1):
        if M[i, i] == 0:
            for j in range(i-1, -1, -1):
                if M[j, i] != 0:
                    M[[i, j]] = M[[j, i]]
                    break

        if M[i, i] == 0:
            continue

        for j in range(i-1, -1, -1):
            M[j] = M[i, i]*M[j] - M[j, i]*M[i]

    for i in range(n):
        M[i] = M[i] / M[i, i]

    X = [M[i, -1] for i in range(n)]
    X = [np.round(x, 6) for x in X]

    return M, X


def solve_using_jordan_elimination():
    n = int(input("\nEnter the number of linear-equations for your system: "))
    rows, cols = n, n + 1

    M = np.array([], dtype=float)

    print(f"\nEnter the {rows}x{cols} Augmented Matrix (A | b):")
    for i in range(rows):
        R = list(map(float, input().split()))
        M = np.append(M, R)

    M = M.reshape((rows, cols))

    row_echelon_matrix_0 = row_echelon(M)
    row_echelon_matrix_1, roots = jordan(M)

    print(f"\nRoots: {roots}\n")


# Test Input
'''
1 2 -1 1 6
-1 1 2 -1 3
2 -1 2 2 14
1 1 -1 2 8
'''
