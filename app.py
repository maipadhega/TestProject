from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    file = open('workwithqueues.py', 'r').read()
    exec(file)
    return "Hello, World!-By Vivek Mahajan. Another change. Trying to add another process"
