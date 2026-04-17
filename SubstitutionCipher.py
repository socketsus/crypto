def encrypt(msg, b):
    msg = msg.upper()
    r = ""
    for ch in msg:
        if ch.isalpha():
            p = ord(ch) - 65
            c = (p + b) % 26
            r += chr(c + 65)
        else:
            r += ch
    return r

def decrypt(msg, b):
    msg = msg.upper()
    r = ""
    for ch in msg:
        if ch.isalpha():
            c = ord(ch) - 65
            p = (c - b) % 26
            r += chr(p + 65)
        else:
            r += ch
    return r

print("Substitution Cipher (Caesar Cipher)")
print("Enter the message to encrypt/decrypt:")
t = input()
print("Enter the shift value (integer):") % 26
b = int(input())
e = encrypt(t, b)
print("Encrypted message:")
print(e)
d = decrypt(e, b)
print("Decrypted message:")
print(d)
