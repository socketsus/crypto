def extended_euclid(a, b):
    if b == 0:
        print("return:", a, 1, 0)
        return a, 1, 0
    g, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    print("Finding inverse of", a, "mod", m)
    g, x, y = extended_euclid(a, m)
    print("gcd:", g, "x:", x, "y:", y)
    if g != 1:
        print("No inverse exists")
        return None
    inv = x % m
    print("Inverse is", inv)
    return inv

a = int(input("Enter a: "))
m = int(input("Enter m: "))
mod_inverse(a, m)
