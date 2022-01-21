from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   
    stream = open("workwithqueues.py")
    read_file = stream.read()
    return exec(read_file)


