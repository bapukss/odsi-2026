import math
from collections import Counter
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(ch, data):
    return AES.new((ch * 16).encode(), AES.MODE_ECB).decrypt(data)

def entropy(data):
    return -sum(c / len(data) * math.log2(c / len(data)) for c in Counter(data).values())

ct = open("slaby_ecb.bin", "rb").read()
ranking = sorted((entropy(decrypt(ch, ct[:4096])), ch) for ch in "abcdefghijklmnopqrstuvwxyz0123456789")
for h, ch in ranking[:5]:
    print(ch, f"{h:.4f}")

print(unpad(decrypt(ranking[0][1], ct), 16).decode())