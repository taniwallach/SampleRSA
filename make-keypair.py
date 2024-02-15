#!/usr/bin/python3

import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
#print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

pubKeyPEM = pubKey.exportKey()
#print(pubKeyPEM.decode('ascii'))

f = open ('testing-public.key', 'w')
f.write(pubKeyPEM.decode('ascii')) #write public key to file
f.close()

#print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()

#print(privKeyPEM.decode('ascii'))

f = open ('testing-private.key', 'w')
f.write(privKeyPEM.decode('ascii')) #write private key to file
f.close()

