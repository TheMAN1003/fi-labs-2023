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
C_test1 = ["еш", "шя", "еы", "до", "зо"]

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
                        listOfPairs.append(
                            [cb(list1[indexX1], alph), cb(list2[indexY1], alph), cb(list1[indexX2], alph),
                             cb(list2[indexY2], alph)])
    return listOfPairs


def solve_system(x1, y1, x2, y2, mod):
    (_, r, _) = extended_gcd(x1 - x2, mod)
    a = (r * (y1 - y2)) % mod
    b = (y1 - a * x1) % mod
    return a, b


def keys(pairs):
    key = []
    mod = len(alph1) ** 2
    for p in pairs:
        key.append(solve_system(p[0], p[1], p[2], p[3], mod))
    return key


def decode(code, a, b, alph):
    text = ""
    m = len(alph)
    (d, a, _) = extended_gcd(a, m**2)
    if d != 1:
        return text
    i = 0
    while i < len(code) - 1:
        x = a*(cb(code[i]+code[i+1], alph) - b) % m**2
        x2 = x % m
        x1 = int((x-x2)/m)
        text += alph[x1]+alph[x2]
        i += 2
    return text


pairs1 = splitOnPairs(M_bi, C_test, alph1)
print(pairs1)
print(len(pairs1))

pairs2 = splitOnPairs(M_bi, C_test, alph2)
print(pairs2)
print(len(pairs2))

k1 = keys(pairs1)
print(k1)
code1 = "эяярэфщкхрстилхфюуцыулнрпяшзрыюуылызцзлглдывэяпщщнивоооооо"

for k in k1:
    print(decode(code1, k[0], k[1], alph1))

k2 = keys(pairs2)
print(k2)

def checkMeaningful(text):
    # о а е ф щ ь
    p = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0,
         'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0,
         'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0,
         'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0,
         'ш': 0, 'щ': 0, 'ы': 0, 'ь': 0, 'э': 0,
         'ю': 0, 'я': 0}
    for letter in text:
        p[letter] += 1
    for i in p:
        p[i] /= len(text)
    i = 0
    bigrams = {}
    while i < len(text) - 1:
        bi = text[i] + text[i+1]
        if bi in bigrams.keys():
            bigrams[bi] += 1
        else:
            bigrams[bi] = 1
        i += 2
    for i in bigrams:
        bigrams[i] /= len(bigrams)
    if p['ф'] < 0.004 and p['щ'] < 0.004 and p['ь'] < 0.012 and p['о'] > 0.1 and p['а'] > 0.06 and p['е'] > 0.08 :
        if bigrams["ст"] > 0.09 and bigrams["но"] > 0.05 and bigrams["то"] > 0.04 and bigrams["на"] > 0.02 and bigrams["ен"] > 0.06 :
            print(text)
            print("next")


def searchThroughKeys(text, keys, alphabet):
    texts = []
    for k in keys:
        texts.append(decode(text, k[0], k[1], alphabet))
    for text in texts:
        checkMeaningful(text)

with open('C:\\Users\\nedoz\\PycharmProjects\\fi-labs-2023\\tasks\\sym_crypto_cp_3\\for_test.utf8\\V3', 'r', encoding="utf8") as f:
    text = f.read()

searchThroughKeys(text, k1, alph1)

searchThroughKeys(text, k2, alph2)