import string
import random

from Crypto.Cipher import AES


key = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

iv = "".join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

# 暗号化
with open("plaintext", "r") as f, open("enc.dat", "wb") as e:
    plaintext = f.read()
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plaintext.encode())
    e.write(cipher_text)

# 復号化
with open("enc.dat", "rb") as f:
    cipher2 = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:-decrypted_text[-1]].decode())
