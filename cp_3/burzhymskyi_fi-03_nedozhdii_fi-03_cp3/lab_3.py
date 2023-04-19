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


alph1 = "абвгдежзийклмнопрстуфхцчшщыьэюя"
alph2 = "абвгдежзийклмнопрстуфхцчшщьыэюя"

M_bi = ["ен", "на", "то", "но", "ст"]
C_test = ["ыя", "йз", "хф", "хр", "ыв"]


def cb(bigram, alphabet):
    n = len(alphabet)
    number = alphabet.index(bigram[0]) * n + alphabet.index(bigram[1])
    return number

def splitOnPairs(list1, list2, alph):
    listOfPairs = []
    for indexX1 in range(len(list1)):
        for indexY1 in range(len(list2)):
            for indexX2 in range(len(list1)):
                for indexY2 in range(len(list2)):
                    if indexX1 != indexX2 and indexY1 != indexY2 and indexX2 < indexX1:
                        listOfPairs.append([cb(list1[indexX1], alph), cb(list2[indexY1], alph), cb(list1[indexX2], alph), cb(list2[indexY2], alph)])
    return listOfPairs


pairs1 = splitOnPairs(M_bi, C_test, alph1)
print(pairs1)
print(len(pairs1))

pairs2 = splitOnPairs(M_bi, C_test, alph2)
print(pairs2)
print(len(pairs2))