#!/usr/bin/python3

import base64
import sys
import time

from Crypto.PublicKey import RSA

from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_v1_5
#from Crypto.Cipher import PKCS1_OAEP

mytime = str(int(time.time()))

key = RSA.import_key(open('testing-public.key').read())

cipher = PKCS1_v1_5.new(key)
#cipher = PKCS1_OAEP.new(key)

sig1 = cipher.encrypt( mytime.encode() );

sig2 = base64.b64encode( sig1 ).decode()

print("Timestamp being encrypted: {ts}\nThe signature is below:\n{sig}".format(ts=mytime,sig=sig2))

