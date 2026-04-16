a, b = map(int, input("Enter two numbers: ").split())
a, b = abs(a), abs(b)

if a < b:
    a, b = b, a

r1 = a
r2 = b

print("q\t r1\t r2\t r")

while r2 != 0:
    q = r1 // r2
    r = r1 % r2
    print(f"{q}\t {r1}\t {r2}\t {r}")
    r1, r2 = r2, r

print("\nGCD =", r1)
