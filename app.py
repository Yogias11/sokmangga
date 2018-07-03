from flask import Flask
app = Flask(__name__)

@app.route('/hello') #contoh
def hello_world():
    return 'Hello, World!'
    
@app.route('/tampil', methods=['GET'])
def hai():
	return "INI ADALAH RETURN DARI PARAMETER PANGGIL"

@app.route('/alimu', methods=['POST'])
def akhir():
	return "Alhamdulillah hiala ni matil iman"


@app.route('/alwan/', methods=['GET'])
def alwan():
    return "<h1>alwan suryansah 1164033 mengerjakan quiz.</p>"

@app.route('/dinda/', methods=['GET'])
def dinda():
    return "<h1>METHODE GET BY DINDA AYU PRATIWI</h1>"
