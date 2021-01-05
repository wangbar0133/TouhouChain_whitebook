from user import CreateAccount
from user import MiningOneBlock
from user import AccountAllCoins
from user import AccountAllTrans
from block import BlockChain, Block
import threading
import socket
import time

botDict = {
    '690f4807e504bbf007d8f296f34c5f02217eda24858d2c5d7a0f118b80134f12': 'be0b74a5af0c277fd5988d3c8050f0365210a6761d5e5c5231916f3ec22a2081',
    '7a58edd936100b0e458f762565279c75bfde3ae1b31b415b1e3516dadd4028f3': '603d2e07951337b1ea6b45410b137543ef5948524d12947b853304f7925d1610',
    'e433fd9db7d4abbcc0205208872162dda2784aab4545910f4bcdcf4dc77a29ff': 'ddc513c4a8b8396061a588a31361a53c598e95d02482cc0de54c9f77a66b47a3',
    '631ab5f71f55483ab8b24b75026a654eddb42f06120599b945d4eeec27da3d64': '06a18862499514c6509b379c9c257b0f3f34c92084302bfb164e57a0d1e4c6dd',
    'dbcc7f167b175043b138c678a3144339b3b826fb90c47ca2b403cf8808c00c95': '35f420452e9db05572dd3a84f12395c166034b2e1b45cd136424159fa433c790',
    'e71fbeddc191c90355918abbc84b71688f38000da1ed2cc82ce056fd691d30c0': '5be1db1454ff27e6f0318a97134908976d9ac297dfa389790c94ff9dc672f618',
    '48b877c1c181b49b2fc45872cfc14bf253bedc8b08dc804c823f5650a8205c8a': 'ce72d41a9ba2e300abea842f0c608622415a10e282b39766eebfa3c2a12fcdc5',
    '6c3e80847a8fa9d3378c733341430b9863a116d69daed2be6d29f2cef94a571b': 'e9b3bb1afd929fb32ff5a1b35cad9ac90aeab53a6f1e7a0f34251eb53592e25d'
}

miner = ['66053664cae16a575ea087ce17c2b400326c366d64580818f14db15b27dbdf86', 'c4d0144731271acf37c33a59d57b1546b66aa633ae98458c5c1766e3b480be2b']

def MingBlock(AccountName):
    blockChainObject = BlockChain()
    blockChainObject.FileTo()
    God = CreateAccount()
    God.FileTo()
    ex_mesg = ""
    global newBlock
    global flag
    flag = 1
    newBlock = MiningOneBlock(AccountName, blockChainObject, God, ex_mesg)
    print("new block succeed!!")
    flag = 0

def TransPool():
    global pool
    pool = []
    PORT = 9999
    udpCliSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpCliSock.bind(('', PORT))
    udpCliSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while flag:
        try:
            data, address = udpCliSock.recvfrom(4096)
            print(str(data) + str(address))
            pool.append(str(data)[2:-1])
        except:
            pass
        time.sleep(0.2)

def miner():
    AccountName = miner[0]
    while True:
        newblockChain = BlockChain()
        newblockChain.FileTo()
        God = CreateAccount()
        God.FileTo()
        ex_mesg = ""
        newBlock = MiningOneBlock(AccountName, newblockChain, God, ex_mesg)
        newblockChain.AddBlockToChain(tx_list=[], newBlock=newBlock)
        newblockChain.ToFile()
        print('已完成')

def listcoins():
    newBlockChain = BlockChain()
    newBlockChain.FileTo()
    AccountName = '66053664cae16a575ea087ce17c2b400326c366d64580818f14db15b27dbdf86'
    coinList = AccountAllCoins(AccountName=AccountName, BlockChain=newBlockChain)
    for coin in coinList:
        print(coin)

def listtarns():
    AccountName = '66053664cae16a575ea087ce17c2b400326c366d64580818f14db15b27dbdf86'
    newBlockChain = BlockChain()
    newBlockChain.FileTo()
    tranList = AccountAllTrans(AccountName, newBlockChain)
    for tran in tranList:
        print(tran)

if __name__ == "__main__":
    #miner()
    listcoins()
    #listtarns()
