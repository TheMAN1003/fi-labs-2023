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

def decode(code,key):
    text = ""
    for i in range(len(code)):
        letter = alphabet[(alphabet.index(code[i]) - alphabet.index(key[i % (len(key))])) % len(alphabet)]
        text += letter

    return text

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


p = {'а': 0.0837222, 'б': 0.0168792, 'в': 0.0439467, 'г': 0.0181161, 'д': 0.031353, 'е': 0.0863102,
     'ж': 0.0122626, 'з': 0.0159467, 'и': 0.0609324, 'й': 0.0106413, 'к': 0.0358363, 'л': 0.0479277,
     'м': 0.0321066, 'н': 0.0644872, 'о': 0.11294, 'п': 0.0280266, 'р': 0.0425652, 'с': 0.0526736,
     'т': 0.063589, 'у': 0.0280076, 'ф': 0.00373739, 'х': 0.00672502, 'ц': 0.00317793, 'ч': 0.0152578,
     'ш': 0.0076803, 'щ': 0.00312845, 'ъ': 0.000216936, 'ы': 0.0175642, 'ь': 0.0208754, 'э': 0.00356613,
     'ю': 0.00785918, 'я': 0.021941}








