from flask import Flask
app = Flask(__name__)
import workwithqueues
@app.route("/")
def hello():

    workwithqueues.createQueue()
    return "created queue successfully"


