import hashlib
import donna25519 as curve25519

class create_account:

    def __init__(self):
        self.bobs_private_key = curve25519.PrivateKey()
        self.bobs_public_key = self.bobs_private_key.get_public()

    def public_key(self):
        return self.bobs_public_key

    def private_key(self):
        return self.bobs_private_key
'''
class sign:

    def
'''