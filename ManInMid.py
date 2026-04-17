p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Alice private key: "))
b = int(input("Bob private key: "))
m = int(input("Mallory private key: "))

A = pow(g, a, p)
B = pow(g, b, p)
M = pow(g, m, p)

print("\n--- Mallory intercepts communication ---")

print("Alice sends A =", A, "but Mallory intercepts it")
print("Bob sends B =", B, "but Mallory intercepts it")

print("\nMallory sends M to Alice and Bob:", M)

alice_key = pow(M, a, p)
bob_key = pow(M, b, p)

mallory_key_A = pow(A, m, p)
mallory_key_B = pow(B, m, p)

print("\nShared Keys:")
print("Alice thinks key =", alice_key)
print("Bob thinks key =", bob_key)

print("\nMallory's Keys:")
print("Mallory-Alice key =", mallory_key_A)
print("Mallory-Bob key =", mallory_key_B)
