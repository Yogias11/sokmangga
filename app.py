from flask import Flask, jsonify
import requests, json
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

@app.route('/instagram/<username>', methods=['GET']) 
def instagram(username):
    uri = 'https://apinsta.herokuapp.com/u/'+username
    response = app.response_class(
        response=requests.get(uri).text,
        mimetype='application/json')
    return response

@app.route('/yas', methods=['PATCH'])
def S():
    return jsonify({'nama' : 'yogi aditya s'})

@app.route('/frdar', methods=['GET'])
def frd():
    return "quiz farid ariyanto saputra"