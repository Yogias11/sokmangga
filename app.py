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

@app.route('/kuis/', methods=['COPY'])
def fikri():
	return "<h2>Ini merupakan kuis web services</h2>"

@app.route('/Frans', methods=['GET'])
def fims():
    return "Keren,Baik, Suka menabung, BERIKUT ADALAH KALIMAT BOHONG"

@app.route('/PUBG', methods=['VIEW'])
def PUBG():
    return "No game,No Life !"


@app.route('/lalita', methods=['GET'])
def lalita():
    return "<h1>JADI ANAK HARUS SOLEH BY LALITA CHANDIANY </h1>"

@app.route('/lidwina', methods=['GET'])
def lid():
    return "lidwina quis"

@app.route('/mifta', methods=['PATCH'])
def miftah():
	return "data PATCH muncul di sini :)"
	
@app.route('/midun', methods=['PATCH'])
def midun():
	return "quis wildan khaustara wijaksana :)"
	
	
@app.route('/sulpa/', methods=['COPY'])
def sulpa():
	return "success"
    
@app.route('/miabb', methods=['VIEW'])
def miabb():
    return "life is a choice"    

@app.route('/nurgivani/', methods=['POST'])
def nurgivani():
    return "Givani done!"

@app.route('/riki', methods=['VIEW'])
def riki():
    return "Hello Quis Web Service :)"

@app.route('/kurnia', methods=['VIEW'])
def kurnia():
    return "I Can do it"

@app.route('/angga', methods=['GET'])
def angg():
    return "quiz hari ini si made angga dwitya p"
	
@app.route('/teduh' , methods=['PATCH'])
def teduh():
    return "Kamu udah makan belum?"

@app.route('/vela/', methods=['GET'])
def vela():
    return "kamu harus kuat"