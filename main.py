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

tx_list_object = ['1', '2', '3', '4', '5', '6']
miner = '12345'
God = CreateAccount()
blockDemo = BlockChain()
blockDemo.HardSetting(hard=5)
hard = blockDemo.Hard
ex_mesg = '123431'

newBlock = Block().CreateStartBlock(hard, miner, God, ex_mesg)

blockDemo.NewChain(newBlock=newBlock, tx_list=tx_list_object)

while True:
    tx_list_object = []
    for i in range(0, 7):
        tx_list_object.append(random.randint(0, 9))
    newBlock = Block().CreateNewBlock(hard, miner, God, ex_mesg, blockDemo)
    blockDemo.AddBlockToChain(newBlock=newBlock, tx_list=tx_list_object)
    time.sleep(1)
    print(blockDemo.GetChain()[-1])
    #blockDemo.PrintBlockChain()