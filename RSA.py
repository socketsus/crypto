def main():
    print("Enter first prime number (p):")
    p = int(input())

    print("Enter second prime number (q):")
    q = int(input())

    n = p * q
    phi = (p - 1) * (q - 1)

    print("Enter public exponent (e) [must be coprime to phi]:")
    e = int(input())
    d = pow(e, -1, phi)

    print(f"Public Key: {{e={e}, n={n}}}")
    print(f"Private Key: {{d={d}, n={n}}}")

    print("\nEnter a message to encrypt:")
    message = input()

    encrypted = []
    for ch in message:
        encrypted.append(pow(ord(ch), e, n))

    print("Encrypted Message:", encrypted)

    decrypted = ""
    for num in encrypted:
        decrypted += chr(pow(num, d, n))

    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()