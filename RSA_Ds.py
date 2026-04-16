def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return -1

p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))
m = int(input("Enter message (integer): "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter public exponent e: "))
d = mod_inverse(e, phi)

signature = pow(m, d, n)
verify = pow(signature, e, n)

print("\n=== RSA ===")
print("Public Key:", (e, n))
print("Private Key:", (d, n))
print("Signature:", signature)
print("Verification:", verify == m)