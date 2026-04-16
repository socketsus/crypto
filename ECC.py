import random

p = int(input("Enter prime p: "))
a = int(input("Enter curve parameter a: "))
b = int(input("Enter curve parameter b: "))

O = (None, None)

def inverse_mod(k, p):
    return pow(k, -1, p)

def is_on_curve(P):
    if P == O:
        return True
    x, y = P
    return (y * y - (x * x * x + a * x + b)) % p == 0

def generate_points():
    points = []
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        for y in range(p):
            if (y*y) % p == rhs:
                points.append((x, y))
    points.append(O)
    return points

def point_add(P, Q):
    if P == O:
        return Q
    if Q == O:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return O

    try:
        if P == Q:
            m = (3 * x1 * x1 + a) * inverse_mod(2 * y1, p) % p
        else:
            m = (y2 - y1) * inverse_mod(x2 - x1, p) % p
    except:
        return O

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

def scalar_mult(k, P):
    R = O
    while k > 0:
        if k % 2 == 1:
            R = point_add(R, P)
        P = point_add(P, P)
        k //= 2
    return R

points = generate_points()
print("\nAll points on curve:")
print(points)

# Input base point
gx = int(input("\nEnter base point Gx: "))
gy = int(input("Enter base point Gy: "))
G = (gx, gy)

if not is_on_curve(G):
    print("Error: G is not on the curve!")
    exit()

# Private key
d = int(input("Enter private key: "))

# Public key
Q = scalar_mult(d, G)
print("Public Key:", Q)

# Message point
mx = int(input("Enter message point x: "))
my = int(input("Enter message point y: "))
M = (mx, my)

if not is_on_curve(M):
    print("Error: Message point is not on curve!")
    exit()

# Encryption
k = int(input("Enter random k: "))
C1 = scalar_mult(k, G)
C2 = point_add(M, scalar_mult(k, Q))

print("\nCipher Text:")
print("C1 =", C1)
print("C2 =", C2)

# Decryption
S = scalar_mult(d, C1)
x, y = S
S_inv = (x, (-y) % p)

M_dec = point_add(C2, S_inv)

print("\nDecrypted Message:", M_dec)