from flask import Flask, request, jsonify
from Communication import communication

app = Flask(__name__)

#Inicializa o flask informando a porta 
def start_flask_server(portToApp):
    app.run(host="0.0.0.0", port=portToApp)


#Rota para receber a solicitação de estado atual do dispositivo, recebendo o seu id
@app.route("/getState/<deviceId>", methods=["GET"])
def getStateDevice(deviceId):
    #Busca o estado atual
    resposta = communication.getActualState(deviceId)

    #Se não houver resposta, devolve erro
    if resposta is None:
        return jsonify({"message":"Erro ao se comunicar com o dispositivo"}), 500
    
    #Se houver resposta, monta mensagem de retorno
    device ={
        "name": resposta.getName(),
        "speed": resposta.getSpeed(),
        "consumption": resposta.getConsumption()
    }
    return jsonify(device), 200

#Pega todos os devices disponiveis no dicionário de devices do broker
@app.route("/devices", methods=["GET"])
def getDevices():
    devicesList = list(communication.devices.keys())
    return jsonify({"devices":devicesList}), 200

#Atualiza o dispositivo através das informações que vem no body
@app.route("/update", methods=["POST"])
def updateDevice():
    data = request.get_json()

    resposta = communication.updateState(data.get("deviceName"), data.get("newSpeed"))

    #Valida se a resposta do dispositivo é um 404, ou seja, algum dado incorreto por parte da aplicação
    if isinstance(resposta, str):
        return jsonify({"message":resposta}), 404
    #Valida se o dispositivo respondeu algo, para mandar resposta adequada a aplicação
    elif resposta is None:
        return jsonify({"message":"Erro ao se comunicar com o dispositivo"}), 500
    device ={
        "name": resposta.getName(),
        "speed": resposta.getSpeed(),
        "consumption": resposta.getConsumption()
    }
    return jsonify(device), 200