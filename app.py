from flask import Flask
app = Flask(__name__)

@app.route('/h', methods=['GET'])
def hello_world():
    return 'Hello, World!'