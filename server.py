import config
from web3 import Web3
from flask import Flask, render_template


app = Flask(__name__)
BLOCK = None


@app.before_request
def getBlock():
    global BLOCK
    try:
        BLOCK = Web3(
            Web3.HTTPProvider(
                endpoint_uri=config.URL
            )
        ).eth.get_block_number()
    except Exception as e:
        print(e)


@app.route("/")
def index():
    print(BLOCK)
    return render_template("index.html", block=BLOCK)


app.run(debug=True)
