a, b = map(int, input("Enter two numbers: ").split())
A, B = a, b
a, b = abs(a), abs(b)

swapped = False
if a < b:
   a, b = b, a
   swapped = True

r1, r2 = a, b
s1, s2 = 1, 0
t1, t2 = 0, 1
print("q\t r1\t r2\t r\t s1\t s2\t s\t t1\t t2\t t")

while r2 != 0:
   q = r1 // r2
   r = r1 % r2
   s = s1 - q * s2
   t = t1 - q * t2
   print(f"{q}\t {r1}\t {r2}\t {r}\t {s1}\t {s2}\t {s}\t {t1}\t {t2}\t {t}")
   r1, r2 = r2, r
   s1, s2 = s2, s
   t1, t2 = t2, t

if swapped:
   s1, t1 = t1, s1

print("\nGCD =", r1)
print("s =", s1)
print("t =", t1)
print(f"\nCheck: {s1}*({A}) + {t1}*({B}) = {s1*A + t1*B}")