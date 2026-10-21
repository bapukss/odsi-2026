from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

password = "haslo-testowe"

def derive(salt):
    return PBKDF2(password.encode("utf-8"), salt, 32, count=200000, hmac_hash_module=SHA256)

def encrypt(data):
    salt, iv = get_random_bytes(16), get_random_bytes(16)
    return salt, iv, AES.new(derive(salt), AES.MODE_CBC, iv).encrypt(pad(data, 16))

def decrypt(salt, iv, ct):
    return unpad(AES.new(derive(salt), AES.MODE_CBC, iv).decrypt(ct), 16)

msg = open("wiadomosc.txt", "rb").read()
for name, data in [("puste", b""), ("16 B", b"0123456789ABCDEF"), ("wiadomosc.txt", msg)]:
    salt, iv, ct = encrypt(data)
    print(name, "rowne:", decrypt(salt, iv, ct) == data, "dlugosc kryptogramu:", len(ct))

c1 = encrypt(msg)[2]
c2 = encrypt(msg)[2]
print("kryptogramy rowne:", c1 == c2)