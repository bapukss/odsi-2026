import hashlib
from pathlib import Path

def sha256_pliku(sciezka):
    return hashlib.sha256(Path(sciezka).read_bytes()).hexdigest()

plik_sum = Path("pliki-dla-studentow/SHA256SUMS.txt")
for wiersz in plik_sum.read_text(encoding="utf-8").splitlines():
    skrot, nazwa = wiersz[:64], wiersz[66:]
    try:
        status = "OK" if sha256_pliku(plik_sum.parent / nazwa) == skrot else "BŁĄD"
    except FileNotFoundError:
        status = "BRAK"
    print(nazwa, status)

h1 = hashlib.sha256("Ala ma kota.".encode("ascii")).digest()
h2 = hashlib.sha256("Ola ma kota.".encode("ascii")).digest()
roznica = int.from_bytes(h1, "big") ^ int.from_bytes(h2, "big")
print("Rozniace sie bity:", bin(roznica).count("1"))