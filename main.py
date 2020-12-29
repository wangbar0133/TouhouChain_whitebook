from flask import Flask, jsonify, render_template, request
from argparse import ArgumentParser
import requests
import time
from block import BlockChain, Block
import random
from user import CreateAccount
'''
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return
'''

tx_list_object = ['      ObjectTransparants', '      ObjectTransparants', '      ObjectTransparants']
miner = '12345'
God = CreateAccount()
blockDemo = BlockChain()
blockDemo.HardSetting(hard=1)
hard = blockDemo.Hard
ex_mesg = ''

newBlock = Block().CreateStartBlock(hard, miner, God, ex_mesg)

blockDemo.NewChain(newBlock=newBlock, tx_list=tx_list_object)

while True:
    newBlock = Block().CreateNewBlock(hard, miner, God, ex_mesg, blockDemo)
    blockDemo.AddBlockToChain(newBlock=newBlock, tx_list=tx_list_object)
    time.sleep(1)
    print(blockDemo.GetChain()[-1])
    blockDemo.ToFile()




'''
blockDemo = BlockChain()
blockDemo.FileTo()
blockDemo.PrintBlockChain()
'''


'''
bc = BlockChain()
bc.FileTo()
print(bc.chain)
#print(God1.SigningKey)
'''