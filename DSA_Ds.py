def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
g = int(input("Enter generator g: "))
x = int(input("Enter private key x: "))
m = int(input("Enter message (integer): "))

y = pow(g, x, p)

k = int(input("Enter random k: "))

r = pow(g, k, p) % q
k_inv = mod_inverse(k, q)

s = (k_inv * (m + x * r)) % q

w = mod_inverse(s, q)

u1 = (m * w) % q
u2 = (r * w) % q

v = (pow(g, u1, p) * pow(y, u2, p)) % p
v %= q

print("\n=== DSA ===")
print("Public Key:", (p, q, g, y))
print("Private Key:", x)
print("Signature:", (r, s))
print("Verification:", v == r)