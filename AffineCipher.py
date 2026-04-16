ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
M = 27

def char_to_num(c):
    return ALPH.index(c)

def num_to_char(n):
    return ALPH[n % M]

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = egcd(b % a, a)
    return g, y - (b // a) * x, x

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    return x % m

def encrypt(msg, a, b):
    msg = msg.upper()
    cipher = ""
    for ch in msg:
        if ch in ALPH:
            p = char_to_num(ch)
            c = (a * p + b) % M
            cipher += num_to_char(c)
        else:
            cipher += ch
    return cipher

def decrypt(msg, a, b):
    inv = modinv(a, M)
    if inv is None:
        raise ValueError(f"a = {a} has no inverse modulo {M}")
    msg = msg.upper()
    plain = ""
    for ch in msg:
        if ch in ALPH:
            c = char_to_num(ch)
            p = (inv * (c - b)) % M
            plain += num_to_char(p)
        else:
            plain += ch
    return plain

text = input("Enter plaintext: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

cipher = encrypt(text, a, b)
print("Ciphertext:", cipher)

plain = decrypt(cipher, a, b)
print("Decrypted :", plain)
