
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x, y) = extended_gcd(b, a % b)
        return (d, y, x - int(a/b) * y)

def solve_linear_mod_equations(a, b, n):
    res = []
    (d, x, y) = extended_gcd(a, n)
    if d == 1:
        res.append((x * b) % n)
    else:
        if b % d == 0:
            (a, b, n) = (a/d, b/d, n/d)
            (_, x, y) = extended_gcd(a, n)
            x_0 = (x * b) % n
            for i in range(d):
                res.append(int(x_0 + i*n))
    return res

print(extended_gcd(2,33))


print(solve_linear_mod_equations(8, 16, 32))

