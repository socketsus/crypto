def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    # Add key letters first
    for ch in key:
        if ch.isalpha() and ch not in used:
            matrix.append(ch)
            used.add(ch)

    # Add remaining alphabet letters
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J excluded
        if ch not in used:
            matrix.append(ch)

    # Convert into 5x5 matrix
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ""

        if i + 1 < len(text):
            b = text[i+1]

        if a == b:
            result += a + "X"
            i += 1
        else:
            if b:
                result += a + b
                i += 2
            else:
                result += a + "X"
                i += 1

    if len(result) % 2 != 0:
        result += "X"

    return result


def find_position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def playfair_encrypt(text, matrix):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            cipher += matrix[r1][(c1+1)%5]
            cipher += matrix[r2][(c2+1)%5]
        elif c1 == c2:  # Same column
            cipher += matrix[(r1+1)%5][c1]
            cipher += matrix[(r2+1)%5][c2]
        else:  # Rectangle rule
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def playfair_decrypt(cipher, matrix):
    text = cipher
    plain = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            plain += matrix[r1][(c1-1)%5]
            plain += matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plain += matrix[(r1-1)%5][c1]
            plain += matrix[(r2-1)%5][c2]
        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


key = input("Enter key: ")
text = input("Enter message: ")

matrix = generate_matrix(key)

print("\nKey Matrix:")
for row in matrix:
    print(row)

encrypted = playfair_encrypt(text, matrix)
print("\nEncrypted:", encrypted)

decrypted = playfair_decrypt(encrypted, matrix)
print("Decrypted:", decrypted)
