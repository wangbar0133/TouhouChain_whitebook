import ed25519
from block import BlockChain, Block, ListToStr, Transactions
import os
import json
import socket
from db import db

class CreateAccount():
    """创建用户对象"""
    def __init__(self):
        self.signing_key, self.verifying_key = ed25519.create_keypair()
        self.PublicKey = self.verifying_key.to_ascii(encoding="hex")
        self.PrivateKey = self.signing_key.to_ascii(encoding="hex")
        self.SigningKey = self.signing_key
        self.VerifiyingKey = self.verifying_key
        self.Username = str(self.PublicKey)[2:-1]
        self.Password = str(self.PrivateKey)[2:-1]
        self.filename = os.getcwd() + '/' + 'God.json'


    def SetGod(self):
        jsonStr = {
            "GodName": str(self.PublicKey),
            "SignKey": str(self.PrivateKey)
        }
        with open(self.filename, 'w') as file_obj:
            json.dump(jsonStr, file_obj)
        file_obj.close()


    def FileTo(self):
        """load god from file"""
        with open(self.filename) as file_obj:
            jsonStr = json.load(file_obj)
            self.PublicKey = bytes(jsonStr["GodName"][2:-1], encoding="utf-8")
            self.PrivateKey = bytes(jsonStr["SignKey"][2:-1], encoding="utf-8")
            self.verifying_key = ed25519.SigningKey(self.PublicKey)
            self.SigningKey = ed25519.SigningKey(self.PrivateKey)


class AccountSearch():
    """用户操作对象"""
    def __init__(self):
        blockChainObj = BlockChain()
        self.chainList = blockChainObj.GetChain()

    def ShowCoins(self, AccountName):
        """一个账户的所有硬币"""
        coinDict = {}
        for block in self.chainList:
            for trans in block['tx']:
                if trans['recive'] == AccountName:
                    for coin in trans['coin_list']:
                        coinDict[coin] = coinDict[coin] + 1 if coin in coinDict else 1
                elif trans['send'] == AccountName:
                    for coin in trans['coin_list']:
                        try:
                            coinDict[coin] = coinDict[coin] - 1
                        except:
                            print('err')
        coinList = []
        for coin in coinDict:
            if coinDict[coin] != 0:
                coinList.append(coin)
        return coinList

    def ShowTransHistory(self, AccountName):
        """一个账户的所有交易记录"""
        tranList = []
        for block in self.chainList:
            tranList = TransFinder(AccountName, block['tx'], tranList)
        return tranList

    def SendCoins(self, SendName, ReciveName, key, coin_list, ex_mesg):
        """发送硬币"""
        HOST = '192.168.1.255'
        PORT = 9999
        ADDR = (HOST, PORT)
        udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpCliSock.bind(('', PORT))
        udpCliSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        data = bytes(Transactions(SendName, key, ReciveName, coin_list, ex_mesg))
        udpCliSock.sendto(data, ADDR)
        udpCliSock.close()


def MiningOneBlock(minerAccount, God, ex_mesg):
    """挖一个块"""
    hard = db().getHard()
    newBlock = Block()
    newBlock.CreateNewBlock(hard, minerAccount, God, ex_mesg)
    return newBlock


def IsAccountExist(AccountName):
    """判断账号是否存在"""
    chainList = db().getChian()
    for block in chainList:
        for trans in block['tx']:
            if trans['recive'] == AccountName or trans['send'] == AccountName:
                return True


def TransFinder(AccountName, transList, tranList):
    """查找一个用户的所有交易记录"""
    for tran in transList:
        if tran['send'] or tran['recive'] == AccountName:
            tranList.append(tran)
    return tranList

def get_host_ip():
    """返回本机IP地址"""
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ss.connect(('8.8.8.8', 8070))
        ip = ss.getsockname()[0]
    finally:
        ss.close()
    return ip



