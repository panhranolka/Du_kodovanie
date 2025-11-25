def cezar_kodovanie(text: str, shift: int) -> str:
    vysledok = ""
    for znak in text:
        if znak.isalpha():
            base = ord("a")
            posunuty = (ord(znak) - base + shift) % 26 + base
            vysledok += chr(posunuty)
        else:
            vysledok += znak
    return vysledok

def cezar_dekodovanie(text: str, shift: int) -> str:
    return cezar_kodovanie(text, -shift)

zak = cezar_kodovanie("dnes je utorok",1000)
dek = cezar_dekodovanie(zak,1000)
print(zak)
print(dek)