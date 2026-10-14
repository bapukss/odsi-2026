import sys

def szyfruj(dane, klucz):
    m = len(klucz)
    return bytes((p + klucz[i % m]) % 256 for i, p in enumerate(dane))

def odszyfruj(dane, klucz):
    m = len(klucz)
    return bytes((c - klucz[i % m]) % 256 for i, c in enumerate(dane))

klucz = b"ZAMEK"

with open(sys.argv[1], "rb") as f:
    zrodlo = f.read()

kryptogram = szyfruj(zrodlo, klucz)
with open("vigenere.bin", "wb") as f:
    f.write(kryptogram)

print("Zgodnosc ze zrodlem:", odszyfruj(kryptogram, klucz) == zrodlo)
print("Puste dane:", odszyfruj(szyfruj(b"", klucz), klucz) == b"")
skrajne = bytes([0, 255, 0, 255])
print("Bajty 0 i 255:", odszyfruj(szyfruj(skrajne, klucz), klucz) == skrajne)

jawny = b"BRAMABRAMABRAMA"
for k in (b"SZYFR", b"KOD"):
    c = szyfruj(jawny, k)
    print(k.decode(), c[0:5].hex(), c[5:10].hex(), c[10:15].hex())