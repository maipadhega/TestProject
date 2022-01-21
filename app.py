from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    file = open('workwithqueues.py', 'r').read()
    return exec(file)
   
