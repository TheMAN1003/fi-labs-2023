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

key = "генацидрусни"