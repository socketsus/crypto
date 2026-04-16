M = 26
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def text_to_nums(text):
    nums = [ALPH.index(c) for c in text.upper() if c.isalpha()]
    print("Text → nums:", nums)
    return nums

def nums_to_text(nums):
    text = ''.join(ALPH[n % M] for n in nums)
    print("Nums → text:", nums, "→", text)
    return text

def pad(nums, n):
    while len(nums) % n != 0:
        nums.append(ALPH.index('X'))
    return nums

def mat_mul(A, B):
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])
    if cA != rB:
        raise ValueError("Incompatible sizes for multiplication")
    R = [[0]*cB for _ in range(rA)]
    for i in range(rA):
        for j in range(cB):
            s = 0
            for k in range(cA):
                s += A[i][k] * B[k][j]
            R[i][j] = s % M
    return R

def mat_det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in A[1:]]
        det += ((-1)**j) * A[0][j] * mat_det(minor)
    return det

def mat_minor(A, r, c):
    return [row[:c] + row[c+1:] for i, row in enumerate(A) if i != r]

def mat_cofactor(A):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = mat_minor(A, i, j)
            C[i][j] = ((-1)**(i+j)) * mat_det(minor)
    return C

def mat_transpose(A):
    return [list(row) for row in zip(*A)]

def mat_inv(A):
    det_raw = mat_det(A)
    det_mod = det_raw % M
    try:
        det_inv = pow(det_mod, -1, M)
    except ValueError:
        raise ValueError(f"Determinant {det_mod} has no inverse modulo {M}. Matrix not invertible.")
    C = mat_cofactor(A)
    adj = mat_transpose(C)
    inv = [[(det_inv * adj[i][j]) % M for j in range(len(A))] for i in range(len(A))]

    print("Determinant (raw):", det_raw)
    print("Determinant mod", M, ":", det_mod)
    print("Determinant inverse mod", M, ":", det_inv)
    print("Cofactor matrix (nested lists):", C)
    print("Adjugate matrix (nested lists):", adj)
    print("Inverse matrix mod", M, ":", inv)
    return inv

def encrypt(plain, key):
    n = len(key)
    nums = pad(text_to_nums(plain), n)
    out = []
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        block_mat = [[x] for x in block]
        enc = mat_mul(key, block_mat)
        enc_flat = [row[0] for row in enc]
        print(f"Encrypt block {i//n}: {block} -> {enc_flat}")
        out.extend(enc_flat)
    cipher_text = nums_to_text(out)
    return cipher_text

def decrypt(cipher, key):
    n = len(key)
    nums = text_to_nums(cipher)
    inv = mat_inv(key)
    out = []
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        block_mat = [[x] for x in block]
        dec = mat_mul(inv, block_mat)
        dec_flat = [row[0] for row in dec]
        print(f"Decrypt block {i//n}: {block} -> {dec_flat}")
        out.extend(dec_flat)
    plain_text = nums_to_text(out)
    return plain_text

n = int(input("Enter n : "))
print(f"Enter {n*n} numbers row-wise for the key matrix:")
vals = list(map(int, input().split()))
if len(vals) != n*n:
    raise ValueError(f"Expected {n*n} numbers, got {len(vals)}")
key = [vals[i*n:(i+1)*n] for i in range(n)]

plain = input("Enter plaintext: ")

cipher = encrypt(plain, key)
print("\nCiphertext:", cipher)

print("\nDecrypted :", decrypt(cipher, key))