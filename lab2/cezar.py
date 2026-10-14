import sys

DRUKOWALNE = set(range(32, 127)) | {9, 10, 13}


def odszyfruj(dane, k):
    return bytes((c - k) % 256 for c in dane)

def ocena(dane):
    return sum(b in DRUKOWALNE for b in dane) / len(dane)

with open(sys.argv[1], "rb") as f:
    dane = f.read()

wyniki = []
for k in range(256):
    tekst = odszyfruj(dane, k)
    wyniki.append((ocena(tekst), k, tekst))

wyniki.sort(key=lambda w: (-w[0], w[1]))
najlepsze = wyniki[:5]

for nr, (o, k, tekst) in enumerate(najlepsze, 1):
    print(f"{nr}. k={k} ocena={o:.4f} {tekst[:60]!r}")

nr = int(input("Wybierz kandydata (1-5): "))
o, k, tekst = najlepsze[nr - 1]

with open("cezar.txt", "wb") as f:
    f.write(tekst)

print(f"Zapisano cezar.txt, k={k}")