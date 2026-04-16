M = 26
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def text_to_nums(text):
   nums = []
   for c in text.upper():
       if c.isalpha():
           nums.append(ALPH.index(c))
   return nums

def nums_to_text(nums):
   text = ''
   for n in nums:
       text += ALPH[n % M]
   return text


def mat_det(A):
   return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def mat_cofactor(A):
   return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]

def find_inv_det(d):
   d = d % M
   for i in range(1, M):
       if (d * i) % M == 1:
           return i
   return None


def mat_mul(A, B):
   rA = len(A)
   cB = len(B[0])
   R = []
   for _ in range(rA):
       row = []
       for _ in range(cB):
           row.append(0)
       R.append(row)
   for i in range(rA):
       for j in range(cB):
           s = 0
           for k in range(len(A[0])):
               s += A[i][k] * B[k][j]
           R[i][j] = s % M
   return R

def mat_transpose(A):
   transposed = []
   for row in zip(*A):
       transposed.append(list(row))
   return transposed

def mat_inv(A):
   det = mat_det(A) % M
   det_inv = pow(det, -1, M)
   C = mat_cofactor(A)
   adj = mat_transpose(C)
   return [[(det_inv * adj[i][j]) % M for j in range(len(A))] for i in range(len(A))]
def pad(nums, n):
   while len(nums) % n != 0:
       nums.append(ALPH.index('X'))
   return nums

def encrypt(plain, key):
   n = len(key)
   nums = pad(text_to_nums(plain), n)
   out = []
   for i in range(0, len(nums), n):
       block = []
       for x in nums[i:i+n]:
           block.append([x])
       enc = mat_mul(key, block)
       for row in enc:
           out.append(row[0])
   return nums_to_text(out)

def decrypt(cipher, key):
   n = len(key)
   nums = text_to_nums(cipher)
   inv = mat_inv(key)
   out = []
   for i in range(0, len(nums), n):
       block = []
       for x in nums[i:i+n]:
           block.append([x])
       dec = mat_mul(inv, block)
       for row in dec:
           out.append(row[0])
   return nums_to_text(out)

n = int(input("Enter n : "))
print(f"Enter {n*n} numbers row-wise for the key matrix:")
vals = list(map(int, input().split()))
key = [vals[i*n:(i+1)*n] for i in range(n)]

plain = input("Enter plaintext: ")
cipher = encrypt(plain, key)

print("\nCiphertext:", cipher)
print("Decrypted :", decrypt(cipher, key))