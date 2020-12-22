import hashlib
import datetime as date
import time
import donna25519 as curve25519

class Encrypt(object):
    @staticmethod
    def hash_encrypt(data_str):
         sha = hashlib.sha256()
         sha.update(data_str)
         return sha.hexdigest()

class create_account:

    def __init__(self):
        self.bobs_private_key = curve25519.PrivateKey()
        self.bobs_public_key = self.bobs_private_key.get_public()

    def public_key(self):
        return self.bobs_public_key.hexdigest()

    def private_key(self):     
        return self.bobs_private_key.hexdigest()

class Block():
    def __init__(self):
        self.block_json = {
                'headers': {
                    'pr_block_hash': None,
                    'hard':None,
                    'var':None,
                    'timestamp':None,
                    'main_chain':True,
                },
                'block_hash':None,
                'tx':[
                ]
            }

        self.tx_json = {
                        'send':None,
                        'recive':None,
                        'timestamp':None,
                        'sign':None,
                        'coin_list':[],
                        'ex_mesg':None
                    }

    def create_start_block(self, block_hash, hard, var):
        self.block_json['hard'] = hard
        self.block_json['block_hash'] = Encrypt.hash_encrypt(str(self.block_json['headers']).encode("utf-8"))
        self.block_json['timestamp'] = time.time()
        pass

    def create_new_block(self, previous_block, block_hash, tx_list, hard):
        self.block_json['block_hash'] = block_hash
        self.block_json['pr_block_hash'] = previous_block['block_hash']
        self.block_json['hard'] = hard
        self.block_json['timestamp'] = time.time()
        for tx in tx_list:
            self.block_json['tx'].append(tx)
        pass    
    
    def __str__(self):
        return "index:"+str(self.index)+"\nprevious_hash:"+self.previous_hash+"\ntimestamp:"+str(self.timestamp)+"\ndata:"+self.data+"\nhash:"+self.hash+"\n\n"
        pass

class BlockCreater(object):
    @staticmethod
    def create_start_block(cls): 
        block = Block() 
        block.create_start_block()
        return block
 
    @staticmethod
    def create_new_block(cls,previous_block,data="new trade data"):
        block = Block()
        block.create_new_block(previous_block,data)
        return block