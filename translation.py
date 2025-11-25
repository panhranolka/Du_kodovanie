# https://py.checkio.org/en/mission/bird-language/share/54d7d6f5263994bb368dded123cae7d8/
sam = "aeiouy"
spol = "qwrtzpsdfghjklxcvbnm"
def translation(retazec):
    counter = 0
    vysledok = ""
    while counter<len(retazec):
        znak = retazec[counter]
        if znak == " ":
            vysledok += " "
            counter += 1
        else:
            vysledok += znak
            if znak in sam:
                counter += 3
            else:
                counter += 2
    return vysledok

print (translation("hieeelalaooo"))
print (translation("hoooowe yyyooouuu duoooiiine"))