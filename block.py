import hashlib
import datetime as date
import time
import donna25519 as curve25519
import random
import ed25519
from user import CreateAccount

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

class Encrypt():

    def hash_encrypt(data_str):
         sha = hashlib.sha256()
         sha.update(data_str)
         return sha.hexdigest()

class Block(): #块对象定义
    def __init__(self):
        self.BlockJson = {
                "headers": {
                    "pr_block_hash": None,
                    "hard": None,
                    "var": None,
                    "timestamp": None,
                    "main_chain": True
                },
                "block_hash": None,
                "tx": [
                ]
            }

        self.tx_list_object = {
                        'send': None,
                        'recive': None,
                        'timestamp': None,
                        'sign': None,
                        'coin_list': [],
                        'ex_mesg': None
                    }

    def CreateStartBlock(self, hard, miner, God, ex_mesg):#创建创世块
        self.BlockJson['headers']['hard'] = hard
        self.BlockJson['headers']['timestamp'] = time.time()
        var = Proof(Block=self.BlockJson, hard=hard)
        self.BlockJson['headers']['var'] = var
        coin_list = MinerCoinList()
        self.BlockJson['block_hash'] = Encrypt.hash_encrypt(str(self.BlockJson['headers']).encode("utf-8"))
        self.BlockJson['tx'].append(Transactions(send=God.PublicKey, SigningKey=God.SigningKey, recive=miner, coin_list=coin_list, ex_mesg=ex_mesg))
        return self.BlockJson

    def CreateNewBlock(self, hard, miner, God, ex_mesg, BlockChain):#增加块
        self.BlockJson['headers']['pr_block_hash'] = BlockChain.chain[-1]['block_hash']
        self.BlockJson['headers']['hard'] = hard
        self.BlockJson['headers']['timestamp'] = time.time()
        var = Proof(Block=self.BlockJson, hard=hard)
        self.BlockJson['headers']['var'] = var
        coin_list = MinerCoinList()
        self.BlockJson['block_hash'] = Encrypt.hash_encrypt(str(self.BlockJson['headers']).encode("utf-8"))
        self.BlockJson['tx'].append(Transactions(send=God.PublicKey, SigningKey=God.SigningKey, recive=miner, coin_list=coin_list, ex_mesg=ex_mesg))
        return self.BlockJson

    def PrintBlock(self):
        print(self.BlockJson)

    def __str__(self):
        return "index:"+str(self.index)+"\nprevious_hash:"+self.previous_hash+"\ntimestamp:"+str(self.timestamp)+"\ndata:"+self.data+"\nhash:"+self.hash+"\n\n"
        pass

class BlockChain():

    def __init__(self):
        self.chain = []

    def HardSetting(self, hard):
        self.Hard = hard

    def NewChain(self, tx_list, newBlock):
        newBlock['tx'] = tx_list
        self.chain.append(newBlock)

    def AddBlockToChain(self, tx_list, newBlock):
        newBlock['tx'] = tx_list
        self.chain.append(newBlock)

    def PrintBlockChain(self):
        for block in self.chain:
            print(block)

    def GetChain(self):
        return self.chain




def Proof(Block, hard):#工作量证明
    while True:
        var = random.randint(1, 10**15)
        Block['headers']['var'] = var
        item = Encrypt.hash_encrypt(str(Block['headers']).encode("utf-8"))
        list_arr = ''
        for s in item:#转化为二进制
            list_arr = list_arr + dict_bin[s]
        if list_arr[0:hard] == '0' * hard:
            return var

def Transactions(send, SigningKey, recive, coin_list, ex_mesg):#SigningKey为SigningKey对象
    timestamp = time.time()
    StrSign = ''
    for item in coin_list:
        StrSign = StrSign + item
    sign = SigningKey.sign(bytes(StrSign, encoding='UTF-8'))
    return {
                'send': send,
                'recive': recive,
                'timestamp': timestamp,
                'sign': sign,
                'coin_list': coin_list,
                'ex_mesg': ex_mesg
            }

def MinerCoinList():
    coinList = []
    for count in range(0, 32):
        coinList.append(Coin())
    return coinList

def Coin():
    return str(random.randint(10**10, 10**11))


aBlock = {'headers': {'pr_block_hash': None, 'hard': 1, 'var': None, 'timestamp': None, 'main_chain': True}, 'block_hash': '15d57c3377040f1de8bd3de6eee1c7003d2f3386f6da7c18317b62fdcb8bf64d', 'tx': [], 'timestamp': 1608626895.2281144}


