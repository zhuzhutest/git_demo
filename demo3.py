# coding: utf-8
import hashlib
from Crypto.Cipher import AES
import base64

class AesCrypter(object):
    def __init__(self):
        self.key = "XXXXXXXXXXXXXXXX"
        self.mode = AES.MODE_CBC
        self.iv = b'0102030405060708'
        print "======"

    def encrypt(self, data):
        data = self.pkcs7padding(data)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted = cipher.encrypt(data)
        return base64.b64encode(encrypted)

    def decrypt(self, data):
        data = base64.b64decode(data)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = cipher.decrypt(data)
        decrypted = self.pkcs7unpadding(decrypted)
        return decrypted

    def pkcs7padding(self, data):
        bs = AES.block_size
        padding = bs - len(data) % bs
        padding_text = chr(padding) * padding
        return data + padding_text

    def pkcs7unpadding(self, data):
        lengt = len(data)
        unpadding = ord(data[lengt - 1])
        return data[0:lengt-unpadding]

if __name__ == '__main__':
    aes = AesCrypter()
    json = "123"
    data = bytes(json)
    for i in data:
        print i
    e = aes.encrypt(data)
    b = bytearray(e)
    print b
    for i in b:
        print i

    de = aes.decrypt(b)
    print de