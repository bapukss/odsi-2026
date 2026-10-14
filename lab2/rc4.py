import itertools
import math
import string
import sys
import time

def rc4(klucz, dane):
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + klucz[i % len(klucz)]) % 256
        s[i], s[j] = s[j], s[i]

    wynik = bytearray()
    i = j = 0
    for b in dane:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        wynik.append(b ^ s[(s[i] + s[j]) % 256])
    return bytes(wynik)


def entropia(dane):
    n = len(dane)
    licznik = [0] * 256
    for b in dane:
        licznik[b] += 1
    return -sum(x / n * math.log2(x / n) for x in licznik if x)


with open(sys.argv[1], "rb") as f:
    kryptogram = f.read()

print("Test dwukrotnego RC4:", rc4(b"abc", rc4(b"abc", kryptogram)) == kryptogram)

probka = kryptogram[:512]
ranking = []
start = time.perf_counter()
for litery in itertools.product(string.ascii_lowercase, repeat=3):
    klucz = "".join(litery).encode()
    ranking.append((entropia(rc4(klucz, probka)), klucz))
czas = time.perf_counter() - start

ranking.sort()

print("Liczba prob:", len(ranking))
print(f"Czas: {czas:.2f} s")
for h, klucz in ranking[:5]:
    print(klucz.decode(), f"{h:.4f}")

klucz = ranking[0][1]
odszyfrowane = rc4(klucz, kryptogram)
with open("rc4.txt", "wb") as f:
    f.write(odszyfrowane)

print("Klucz:", klucz.decode())
print(repr(odszyfrowane[:200]))
print("Ponowne szyfrowanie zgodne:", rc4(klucz, odszyfrowane) == kryptogram)
print(f"Entropia kryptogramu: {entropia(kryptogram):.4f}")
print(f"Entropia odszyfrowania: {entropia(odszyfrowane):.4f}")