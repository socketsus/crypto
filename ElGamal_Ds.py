def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

p = int(input("Enter prime p: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
m = int(input("Enter message (integer): "))

y = pow(g, x, p)

k = int(input("Enter random k: "))
while mod_inverse(k, p - 1) == -1:
    k += 1

r = pow(g, k, p)
k_inv = mod_inverse(k, p - 1)

s = (k_inv * (m - x * r)) % (p - 1)

left = pow(g, m, p)
right = (pow(y, r, p) * pow(r, s, p)) % p

print("\n=== ElGamal ===")
print("Public Key:", (p, g, y))
print("Private Key:", x)
print("Signature:", (r, s))
print("Verification:", left == right)