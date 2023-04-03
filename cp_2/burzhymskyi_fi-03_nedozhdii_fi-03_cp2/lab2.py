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


