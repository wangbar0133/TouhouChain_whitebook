from flask import Flask, jsonify, render_template, request
from argparse import ArgumentParser
import requests
import time
from block import BlockChain, Block
import random
from user import CreateAccount
from user import IsAccountExist
from client import showAllCoins
from client import showAllTransHistory

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('hello.html')

@app.route('/account/',methods=['POST','GET'])
def account():
    #username = '66053664cae16a575ea087ce17c2b400326c366d64580818f14db15b27dbdf86'
    resp = request.form.getlist('username')
    try:
        username = resp[0]
    except:
        username = 'err'
    if not IsAccountExist(username):
        coinList = '请输入存在的账号'
    else:
        coinList = showAllCoins(AccountName=username)
    return render_template('account.html',
                           coinList=coinList)

@app.route('/createaccount/',methods=['POST','GET'])
def createaccount():
    newAccount = CreateAccount()
    return render_template('createaccount.html',
                           username=newAccount.Username,
                           password=newAccount.Password)

@app.route('/tran/',methods=['POST','GET'])
def tran():
    return render_template('tran.html')

@app.route('/mine/',methods=['POST','GET'])
def mine():
    return render_template('mine.html')

if __name__ == '__main__':
    app.run(debug=True)