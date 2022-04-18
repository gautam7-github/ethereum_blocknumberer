from time import sleep
import config
from web3 import Web3
from flask import Flask, render_template


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
    # print(BLOCK)
    return render_template("block.html", block=BLOCK)


app.run(debug=True)
