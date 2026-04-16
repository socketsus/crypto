def mat_det(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0
    for j in range(len(A)):
        minor = []
        for row in A[1:]:
            minor.append(row[:j] + row[j+1:])
        det += ((-1) ** j) * A[0][j] * mat_det(minor)
    return det

def mat_minor(A, r, c):
    minor = []
    for i, row in enumerate(A):
        if i != r:
            minor.append(row[:c] + row[c+1:])
    return minor

def mat_cofactor(A):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = ((-1) ** (i + j)) * mat_det(mat_minor(A, i, j))
    return C

def mat_transpose(A):
    transposed = []
    for row in zip(*A):
        transposed.append(list(row))
    return transposed

def modular_matrix_inverse(A, M):
    det = mat_det(A) % M
    det_inv = pow(det, -1, M)
    C = mat_cofactor(A)
    adj = mat_transpose(C)
    return [[(det_inv * adj[i][j]) % M for j in range(len(A))] for i in range(len(A))]

if __name__ == "__main__":
    n = int(input("Enter n (matrix size): "))
    M = int(input("Enter modulus M: "))
    print(f"Enter {n*n} numbers row-wise for the matrix:")
    vals = list(map(int, input().split()))
    A = [vals[i*n:(i+1)*n] for i in range(n)]
    try:
        inv = modular_matrix_inverse(A, M)
        print("Inverse matrix:")
        for row in inv:
            print(row)
    except ValueError:
        print("Matrix is not invertible modulo", M)
