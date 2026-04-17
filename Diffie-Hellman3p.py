p = int(input("Enter a prime number (P): "))
g = int(input("Enter a primitive root (G): "))

a = int(input("Alice: Enter private key (a): "))
b = int(input("Bob: Enter private key (b): "))
c = int(input("Charlie: Enter private key (c): "))

A = (g ** a) % p
B = (g ** b) % p
C = (g ** c) % p

print("\nPublic Keys:")
print("Alice sends:", A)
print("Bob sends:", B)
print("Charlie sends:", C)

AB = (B ** a) % p
BC = (C ** b) % p
CA = (A ** c) % p

print("\nIntermediate Keys:")
print("Alice computes B^a mod p:", AB)
print("Bob computes C^b mod p:", BC)
print("Charlie computes A^c mod p:", CA)

KA = (BC ** a) % p
KB = (CA ** b) % p
KC = (AB ** c) % p

print("\nFinal Shared Secret Keys:")
print("Alice's Secret:", KA)
print("Bob's Secret:", KB)
print("Charlie's Secret:", KC)
