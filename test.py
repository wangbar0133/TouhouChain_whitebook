import hashlib
import donna25519 as curve25519
import binascii
import time
'''
bobs_private=curve25519.PrivateKey()
bobs_public=bobs_private.get_public()

print(binascii.hexlify(bobs_private.private))
'''

import hashlib
import random
import os,sys

dict_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 2)
        mid.append(base[rem])


def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))


def hash_encrypt(data_str):
         sha = hashlib.sha256()
         sha.update(data_str)
         return sha.hexdigest()

headers = "{'pr_block_hash': None,"


def str2hex(text):
    '''将字符串转换为十六进制数'''
    if not isinstance(text, (str, bytes)):
        raise TypeError('input is not a str type')
    if isinstance(text, str):
        data = text.encode('utf8')
    else:
        data = text[:]
    return ''.join(map(lambda x: hex(x)[2:], data))

time1 = time.time()
count = 0
while True:
    before = headers + str(random.randint(1, 10**15))
    item = hash_encrypt(before.encode("utf8"))
    list_arr = ''
    for s in item:
        list_arr = list_arr + dict_bin[s]
    i = 18
    print(list_arr[0:i])
    count = count + 1
    if list_arr[0:i] == '0' * (i):
        break
time2 = time.time() - time1
print("..........................")
print("suc" + str(time2))
print(count / time2)
