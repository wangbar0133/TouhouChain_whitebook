from user import MiningOneBlock, CreateAccount
from block import BlockChain, Block
import threading
import socket
import time
import click

def MingBlock(AccountName):
    """在指定用户名下挖一个块,返回一个块对象"""
    God = CreateAccount()  # 创建一个用户对象
    God.FileTo()
    ex_mesg = ""
    global newBlock
    global flag
    flag = 1
    newBlock = MiningOneBlock(AccountName, God, ex_mesg)
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

def DomMining(accountname):
    global flag
    flag = 1
    while True:
        ThreadMining = threading.Thread(target=MingBlock, args=(accountname,))
        ThreadPool = threading.Thread(target=TransPool)
        ThreadMining.start()
        ThreadPool.start()
        ThreadPool.join()
        newBlock.insertTrans(tx_list=pool)
        BlockChain().AddBlockToChain(newBlock=newBlock)
        print('connect to chain')

@click.command()
@click.option('--accountname')
def go(accountname):
    DomMining(accountname)

if __name__ == '__main__':
    go()



