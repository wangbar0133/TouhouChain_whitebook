import hashlib
import datetime as date
import time
import donna25519 as curve25519
import random
import ed25519
import json
import os

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
                    "pr_block_hash": "",
                    "hard": "",
                    "var": "",
                    "timestamp": "",
                    "main_chain": 'True'
                },
                "block_hash": "",
                "tx": [
                ]
            }

        self.tx_list_object = {
                        'send': "",
                        'recive': "",
                        'timestamp': "",
                        'sign': "",
                        'coin_list': [],
                        'ex_mesg': ""
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
        self.filename = os.getcwd() + '/' + 'blockchain.json'
        self.Hard = 20

    def HardSetting(self, hard):
        self.Hard = hard

    def NewChain(self, tx_list, newBlock):
        newBlock['tx'] = newBlock['tx'] + tx_list
        self.chain.append(newBlock)

    def AddBlockToChain(self, tx_list, newBlock):
        newBlock['tx'] = newBlock['tx'] + tx_list
        self.chain.append(newBlock)

    def PrintBlockChain(self):
        for block in self.chain:
            print(block)

    def GetChain(self):
        return self.chain

    def ToFile(self):
        with open(self.filename, 'w') as file_obj:
            jsonStr = json.loads(ListToStr(self.chain))
            json.dump(jsonStr, file_obj)
        file_obj.close()

    def FileTo(self):
        with open(self.filename) as file_obj:
            self.chain = json.load(file_obj)


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
    sign = SigningKey.sign(bytes(StrSign, encoding='UTF-8'), encoding="base64")
    return {
                'send': str(send)[2:-1],
                'recive': recive,
                'timestamp': timestamp,
                'sign': str(sign)[2:-1],
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

def ListToStr(Lists):
    Str = '['
    for item in Lists:
        Str = Str + str(item) + ','
    Str = Str[0:-1] + ']'
    Str = Str.replace("'", '"')
    return Str

aBlock = {'headers': {'pr_block_hash': '3b91b6938d5b6a7b9645611874be5d022cb3cb9af5f0590cf2053cb6f35bc9ea', 'hard': 1, 'var': 720738739358122, 'timestamp': 1608842036.1920986, 'main_chain': 'True'}, 'block_hash': '3263111648f7ce7847fc743223596e93858d187bf108a5615f3514fd5baff09f', 'tx': [{'send': '58ba2ed0693b7baecfd0c92db251590d7775de63e28096c11e526868cfe11e8a', 'recive': '12345', 'timestamp': 1608842036.192287, 'sign': 'SmS3r3f3enx1AZUsxXSeV2fLfwfWKuJB9NuRG+KHZ0cCjm2rkRmnQr76YzsvBN4yOBndy7o/RI9kt9tyQKojCQ', 'coin_list': ['32539285717', '48046208218', '93758500636', '68358694043', '88125517036', '63140560766', '49995213343', '41330701359', '68194671875', '19797954981', '40474943768', '44521762831', '83376898157', '44857506899', '57136310768', '45220503968', '36227252573', '61770945398', '26074468478', '19388423054', '69571467589', '72818500124', '29998650638', '53597662402', '17580075653', '45152793882', '17044176202', '31314570275', '76790005252', '22710646889', '69289118732', '53587951571'], 'ex_mesg': ''}, '      ObjectTransparants', '      ObjectTransparants', '      ObjectTransparants']}


