import time
import random
import json
import os
from bin import Encrypt
from bin import ListToStr
from bin import Trans16To2
from db import db


class Block():
    """块对象"""
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

    def CreateNewBlock(self, hard, miner, God, ex_mesg):  # 增加块
        try:
            self.BlockJson['headers']['pr_block_hash'] = BlockChain().getTopBlock()['block_hash']
        except:
            pass
        self.BlockJson['headers']['hard'] = hard
        self.BlockJson['headers']['timestamp'] = time.time()
        var = Proof(Block=self.BlockJson, hard=hard)
        self.BlockJson['headers']['var'] = var
        coin_list = MinerCoinList()
        self.BlockJson['block_hash'] = Encrypt().HashEncrypt(str(self.BlockJson['headers']).encode("utf-8"))
        self.BlockJson['tx'].append(Transactions(send=God.PublicKey, SigningKey=God.SigningKey, recive=miner, coin_list=coin_list, ex_mesg=ex_mesg))

    def PrintBlock(self):
        print(self.BlockJson)

    def insertTrans(self, tx_list):
        self.BlockJson["tx"].append(tx_list)


class BlockChain(db):
    """一个区块链类，不是对象"""
    def AddBlockToChain(self, newBlock):
        blockJson = newBlock.BlockJson
        self.insert(blockJson)

    def PrintBlockChain(self):
        for block in self.getChian():
            print(block)


def Proof(Block, hard):
    """工作量证明"""
    while True:
        var = random.randint(1, 10**15)
        Block['headers']['var'] = var
        item = Encrypt().HashEncrypt(str(Block['headers']).encode("utf-8"))
        list_arr = Trans16To2().do(item)
        if list_arr[0:hard] == '0' * hard:
            return var


def Transactions(send, SigningKey, recive, coin_list, ex_mesg):  #  SigningKey为SigningKey对象
    """返回一个交易里面的交易json对象"""
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
    """挖矿奖励的硬币列表"""
    coinList = []
    for count in range(0, 32):
        coinList.append(Coin())
    return coinList


def Coin():
    """一个硬币"""
    return str(random.randint(10**10, 10**11))
