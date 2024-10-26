import numpy as np


def row_echelon(Augmented_Matrix: np.ndarray):
    try:
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

    except Exception as e:
        print("Error in row_echelon:", e)
        return None


def gauss(Augmented_Matrix: np.ndarray) -> tuple[np.ndarray, list[float]]:
    try:
        M = row_echelon(Augmented_Matrix)
        n, _ = M.shape

        for i in range(n):
            M[i] = M[i] / M[i, i]

        X = [0] * n

        for i in range(n-1, -1, -1):
            S = np.sum([M[i, j]*X[j] for j in range(n) if i != j])
            X[i] = M[i, -1] - S

        X = [np.round(x, 6) for x in X]

        return M, X

    except Exception as e:
        print("Error in gauss:", e)
        return None, None


def solve_using_gaussian_elimination_method():
    try:
        n = int(input("\nEnter the number of linear-equations for your system: "))
        rows, cols = n, n + 1

        M = np.array([], dtype=float)

        print(f"\nEnter the {rows}x{cols} Augmented Matrix (A | b):")
        for i in range(rows):
            R = list(map(float, input().split()))
            M = np.append(M, R)

        M = M.reshape((rows, cols))

        row_echelon_matrix_0 = row_echelon(M)
        row_echelon_matrix_1, roots = gauss(M)

        print(f"\nRoots: {roots}\n")

    except Exception as e:
        print("Error in solve_using_gaussian_elimination_method:", e)
        return None
