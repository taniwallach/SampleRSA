#!/usr/bin/python3

import base64
import sys

from Crypto.PublicKey import RSA

from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_v1_5
#from Crypto.Cipher import PKCS1_OAEP

base64_ciphertext = str(sys.argv[1])

ciphertext = base64.b64decode(  base64_ciphertext  )

key = RSA.import_key(open('testing-private.key').read())

cipher = PKCS1_v1_5.new(key)
#cipher = PKCS1_OAEP.new(key)

sentinel = get_random_bytes(16)

plaintext = cipher.decrypt(ciphertext, sentinel).decode()

print('The decrypted data is: {pt}'.format(pt=plaintext))
