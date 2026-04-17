# Diffie-Hellman Key Exchange 
p = int(input("Enter a prime number (P): "))
g = int(input("Enter a primitive root (G): "))

a = int(input("Alice: Enter private key (a): "))
b = int(input("Bob: Enter private key (b): "))
# Public Keys
# A = g^a mod p
A = (g ** a) % p
# B = g^b mod p
B = (g ** b) % p
print("Alice sends to Bob:", A)
print("Bob sends to Alice:", B)
# Shared Secret Keys
# K_A = B^a mod p
keyA = (B ** a) % p
# K_B = A^b mod p
keyB = (A ** b) % p
print("\nShared Secrets:")
print("Alice's Secret Key:", keyA)
print("Bob's Secret Key:", keyB)
