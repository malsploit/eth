#!/usr/bin/env python3
import sys
import binascii
import hashlib
import hmac
import struct
import requests 
from ethereum.utils import privtoaddr
from base58 import b58encode_check
from ecdsa.curves import SECP256k1
def read_file_parse_ip():
	for line in open(sys.argv[1], 'r'):
		pubkey = line.strip().rstrip('\n')
		private_key = pubkey
		pubkey = privtoaddr(private_key).hex()
		r = requests.get('https://api.etherscan.io/api?module=account&action=balance&address=0x'+pubkey+'&tag=latest&apikey=YourApiKeyToken')
		print (pubkey+" "+r.text)
read_file_parse_ip()
