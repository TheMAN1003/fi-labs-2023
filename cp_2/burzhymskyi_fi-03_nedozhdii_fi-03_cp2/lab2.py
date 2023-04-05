alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def redact_text():
    text = ""
    with open('balobol.txt', 'r', encoding="utf8") as f:
        line = f.read()
        line = line.lower()
        new_line = ""
        for letter in line:
            if letter >= 'а' and letter <= 'я':
                new_line += letter
        text += new_line

    with open('balobol_clean.txt', 'w', encoding="utf8") as f:
        f.write(text)

with open('balobol_clean.txt', 'r', encoding="utf8") as f:
    text = f.read()


key_2 = "ру"
key_3 = "чвк"
key_4 = "груз"
key_5 = "гойда"

key_12 = "генацидрусни"

def encode(text, key):
    code = ""
    for i in range(len(text)):
        letter = alphabet[(alphabet.index(text[i]) + alphabet.index(key[i % (len(key))])) % len(alphabet)]
        code += letter
    with open('balobol_encoded_12.txt', 'w', encoding="utf8") as f:
        f.write(code)

    return code

def N(Y,t):
    k = 0
    for i in Y:
        if i == t:
            k += 1
    return k

def IoC(Y):
    k = 0
    n = len(Y)
    for t in alphabet:
        tmp = N(Y,t)
        k += (tmp * (tmp - 1))
    k = float(k / (n * (n - 1)))
    return k

print(IoC(text))
print(IoC(encode(text,key_2)))
print(IoC(encode(text,key_3)))
print(IoC(encode(text,key_4)))
print(IoC(encode(text,key_5)))
print(IoC(encode(text,key_12)))


def lenKey(Y):
    n = len(Y)
    D = []
    for r in range(6, n):
        D.append(0)
        if n % r == 0:
            for i in range(0, n-r):
                if(Y[i] == Y[i+r]):
                    D[r-6] += 1
    print(D)
    return D.index(max(D))+6


with open('labtext_encoded', 'r', encoding="utf8") as f:
    text = f.read()

print(lenKey(text))

