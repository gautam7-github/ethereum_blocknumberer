from time import sleep

from flask import Flask, render_template
from web3 import Web3

import config

app = Flask(__name__)
BLOCK = None
web3Client = Web3(
    Web3.HTTPProvider(
        endpoint_uri=config.URL
    )
)


@app.before_request
def getBlock():
    global BLOCK
    try:
        BLOCK = web3Client.eth.get_block_number()
    except Exception as e:
        print(e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getBlock")
def index():
    return render_template("block.html", block=BLOCK)


app.run(debug=True)
