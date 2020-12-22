import hashlib
import random

def hash_encrypt(data_str):
         sha = hashlib.sha256()
         sha.update(data_str)
         return sha.hexdigest()

print(random.randint(1, 10**10))