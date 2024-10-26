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


def jordan(Augmented_Matrix: np.ndarray):
    try:
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

        return X

    except Exception as e:
        print("Error in jordan:", e)
        return None


def solve_using_jordan_elimination_method():
    try:
        n = int(input("\nEnter the number of linear-equations for your system: "))
        rows, cols = n, n + 1

        M = np.array([], dtype=float)

        print(f"\nEnter the {rows}x{cols} Augmented Matrix (A | b):")
        for i in range(rows):
            R = list(map(float, input().split()))
            M = np.append(M, R)

        M = M.reshape((rows, cols))

        roots = jordan(M)

        print(f"\nRoots: {roots}\n")

    except Exception as e:
        print("Error in solve_using_jordan_elimination_method:", e)
        return None
