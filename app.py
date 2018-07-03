from flask import Flask
app = Flask(__name__)

@app.route('/hello') #contoh
def hello_world():
    return 'Hello, World!'