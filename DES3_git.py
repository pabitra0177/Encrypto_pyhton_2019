## pip install pycrypto`

from Crypto.Cipher import DES3
from Crypto import Random
key = 'Sixteen byte key'
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = 'sona si latine loqueri  ' #padded with spaces so than len(plaintext) is multiple of 8
encrypted_text = cipher_encrypt.encrypt(plaintext)

cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
cipher_decrypt.decrypt(encrypted_text)
cipher_decrypt.decrypt(encrypted_text) #you cant do it twice

"""
For MODE_ECB, MODE_CBC, and MODE_OFB, plaintext length (in bytes) must be a multiple of block_size.
For MODE_CFB, plaintext length (in bytes) must be a multiple of segment_size/8.
For MODE_CTR, plaintext can be of any length.
For MODE_OPENPGP, plaintext must be a multiple of block_size, unless it is the last chunk of the message.
key size (must be either 16 or 24 bytes long)
"""
"""
https://pythonhosted.org/pycrypto/Crypto.Cipher.DES3-module.html
https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation
"""

