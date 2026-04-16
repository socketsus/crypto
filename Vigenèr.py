def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypt(text, key):
    cipher = ""

    for i in range(len(text)):
        p = ord(text[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        c = (p + k) % 26
        cipher += chr(c + ord('A'))

    return cipher


def decrypt(cipher, key):
    text = ""

    for i in range(len(cipher)):
        c = ord(cipher[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        p = (c - k) % 26
        text += chr(p + ord('A'))

    return text


# Input
plaintext = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

key = generate_key(plaintext, key)

cipher = encrypt(plaintext, key)
print("Ciphertext:", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted text:", decrypted)
