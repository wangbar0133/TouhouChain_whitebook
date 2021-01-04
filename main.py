from flask import Flask, jsonify, render_template, request
from argparse import ArgumentParser
import requests
import time
from block import BlockChain, Block
import random
from user import CreateAccount
from client import showAllCoins
from client import showAllTransHistory

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('hello.html')

@app.route('/account/',methods=['POST','GET'])
def account():
    username = request.form.getlist('username')[0]
    accountList = showAllCoins(AccountName=username)
    return render_template('account.html',
                           coinList=accountList)

@app.route('/createaccount/',methods=['POST','GET'])
def createaccount():
    newAccount = CreateAccount()
    return render_template('createaccount.html',
                           username=newAccount.Username,
                           password=newAccount.Password)

@app.route('/tran/',methods=['POST','GET'])
def tran():
    return

if __name__ == '__main__':
    app.run(debug=True)