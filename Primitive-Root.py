import math

# Prime checking function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Primitive roots function
def primitive_roots(p):
    print("Primitive roots are:")
    
    for g in range(2, p):
        values = []
        
        for i in range(1, p):
            values.append((pow(g, i, p)))
        
        if len(set(values)) == p - 1:
            print(g, end=" ")


p = int(input("Enter a prime number: "))

if is_prime(p):
    primitive_roots(p)
else:
    print("Not a prime number")