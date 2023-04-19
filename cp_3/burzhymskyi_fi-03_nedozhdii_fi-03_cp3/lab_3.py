def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        (d, x, y) = extended_gcd(b, a % b)
        return d, y, x - int(a / b) * y


def solve_linear_mod_equations(a, b, n):
    res = []
    (d, x, y) = extended_gcd(a, n)
    if d == 1:
        res.append((x * b) % n)
    else:
        if b % d == 0:
            (a, b, n) = (a / d, b / d, n / d)
            (_, x, y) = extended_gcd(a, n)
            x_0 = (x * b) % n
            for i in range(d):
                res.append(int(x_0 + i * n))
    return res


alph = "абвгдежзийклмнопрстуфхцчшщыьэюя"
alph1 = "абвгдежзийклмнопрстуфхцчшщьыэюя"

M_bi = ["ен", "на", "то", "но", "ст"]
C_test = ["ыя", "йз", "хф", "хр", "ыв"]


def convert_bigrams(bigrams):
    num1 = []
    num2 = []
    n = len(alph)
    for i in bigrams:
        num1.append(alph.index(i[0]) * n + alph1.index(i[1]))
        num2.append(alph1.index(i[0]) * n + alph1.index(i[1]))
    return num1, num2


(m1, m2) = convert_bigrams(M_bi)

print(m1,m2)

(c1, c2) = convert_bigrams(C_test)

print(c1,c2)
