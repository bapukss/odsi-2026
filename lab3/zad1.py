from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"0123456789ABCDEF" * 4
key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
iv = get_random_bytes(16)

for name, new in [("ECB", lambda: AES.new(key, AES.MODE_ECB)), ("CBC", lambda: AES.new(key, AES.MODE_CBC, iv))]:
    ct = new().encrypt(data)
    blocks = [ct[i:i + 16] for i in range(0, 64, 16)]
    print(name)
    for i, b in enumerate(blocks, 1):
        print(i, b.hex())
    print("powtorzenia:", [[j + 1 for j, c in enumerate(blocks) if c == b] for b in set(blocks) if blocks.count(b) > 1])
    print("rowne po odszyfrowaniu:", new().decrypt(ct) == data)
