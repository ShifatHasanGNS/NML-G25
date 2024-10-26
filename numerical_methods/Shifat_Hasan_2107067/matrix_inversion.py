import numpy as np


def complete_row_echelon(matrix: np.ndarray) -> np.ndarray:
    try:
        M = np.hstack((matrix, np.eye(matrix.shape[0])))

        n, _ = M.shape

        for i in range(n):
            if M[i, i] == 0:
                for j in range(i+1, n):
                    if M[j, i] != 0:
                        M[[i, j]] = M[[j, i]]
                        break
            if M[i, i] == 0:
                continue
            for j in range(i+1, n):
                M[j] = M[i, i]*M[j] - M[j, i]*M[i]

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

        return M

    except Exception as e:
        print("Error in complete_row_echelon:", e)
        return None


def inverse_matrix():
    try:
        n = int(input("\nEnter the dimension of the matrix: "))
        rows, cols = n, n

        M = np.array([], dtype=float)

        print(f"\nEnter the {rows}x{cols} Matrix:")
        for i in range(rows):
            R = list(map(float, input().split()))
            M = np.append(M, R)

        M = M.reshape((rows, cols))

        normal_form = complete_row_echelon(M)

        print(f"\nInverse Matrix:\n{normal_form[:, n:]}\n")

    except Exception as e:
        print("Error in inverse_matrix:", e)
        return None
