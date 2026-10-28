import hashlib
import hmac
import secrets
from pathlib import Path

baza = {}
for wiersz in Path("pliki-dla-studentow/hasla.txt").read_text(encoding="utf-8").splitlines():
    login, iteracje, sol, skrot = wiersz.split(":")
    baza[login] = (int(iteracje), bytes.fromhex(sol), bytes.fromhex(skrot))

def weryfikuj(login, haslo):
    if login not in baza:
        return False
    iteracje, sol, skrot = baza[login]
    wynik = hashlib.pbkdf2_hmac("sha256", haslo.encode("utf-8"), sol, iteracje)
    return hmac.compare_digest(wynik, skrot)

def dodaj(login, haslo):
    sol = secrets.token_bytes(16)
    skrot = hashlib.pbkdf2_hmac("sha256", haslo.encode("utf-8"), sol, 600000)
    baza[login] = (600000, sol, skrot)
    return f"{login}:600000:{sol.hex()}:{skrot.hex()}"

print(weryfikuj("anna", "Kasztan-2026"))
print(weryfikuj("anna", "kasztan-2026"))
print(weryfikuj("piotr", "Żółw na łące"))
print(weryfikuj("kasia", "Kasztan-2026"))

dodaj("test1", "Haslo-123")
dodaj("test2", "Haslo-123")
print("Sole rowne:", baza["test1"][1] == baza["test2"][1])
print("Skroty rowne:", baza["test1"][2] == baza["test2"][2])
print(weryfikuj("test1", "Haslo-123"))
print(weryfikuj("test2", "Haslo-123"))