import hashlib
from pathlib import Path

def h24(dane):
    return hashlib.sha256(dane).hexdigest()[:6]

def wariant(wiersze, v):
    return b"".join(w + (b" " if (v >> i) & 1 else b"") + b"\n" for i, w in enumerate(wiersze))

oryginal = Path("pliki-dla-studentow/oryginal.txt").read_bytes()[:-1].split(b"\n")
zmieniony = Path("pliki-dla-studentow/zmieniony.txt").read_bytes()[:-1].split(b"\n")

slownik = {}
for v in range(8192):
    slownik[h24(wariant(oryginal, v))] = v

h0 = h24(wariant(oryginal, 0))
para = None
licznik = 0
for v in range(8192):
    h = h24(wariant(zmieniony, v))
    if para is None and h in slownik:
        para = (slownik[h], v, h)
    if h == h0:
        licznik += 1

print("Para:", para)
print("Warianty z h24 oryginalu:", licznik)