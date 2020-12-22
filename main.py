from flask import Flask, jsonify,render_template,request
from argparse import ArgumentParser
import requests

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return

