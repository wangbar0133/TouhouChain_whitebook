from user import MiningOneBlock, CreateAccount
from block import BlockChain, Block
import threading
import socket
import time
import click

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

@click.command()
@click.option('--accountname')
def go(accountname):
    global flag
    flag = 1
    while True:
        blockChain = BlockChain()
        blockChain.FileTo()
        ThreadMining = threading.Thread(target=MingBlock, args=(accountname,))
        ThreadPool = threading.Thread(target=TransPool)
        ThreadMining.start()
        ThreadPool.start()
        ThreadPool.join()
        blockChain.AddBlockToChain(newBlock=newBlock, tx_list=pool)
        blockChain.ToFile()
        click.echo('connect to chain')

if __name__ == '__main__':
    go()



