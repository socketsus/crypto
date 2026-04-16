import hashlib

text = input("Enter text: ")

# SHA-1
sha1_hash = hashlib.sha1(text.encode()).hexdigest()

# SHA-512
sha512_hash = hashlib.sha512(text.encode()).hexdigest()

print("\n=== HASH OUTPUTS ===")
print("SHA-1   :", sha1_hash)
print("SHA-512 :", sha512_hash)

print("\n=== LENGTH COMPARISON ===")
print("SHA-1 length   :", len(sha1_hash), "hex characters")
print("SHA-512 length :", len(sha512_hash), "hex characters")

print("\n=== ANALYSIS ===")
print("SHA-1 produces 160-bit hash (40 hex chars)")
print("SHA-512 produces 512-bit hash (128 hex chars)")