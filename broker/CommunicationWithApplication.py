from flask import Flask, request, jsonify
from Communication import communication

app = Flask(__name__)

def start_flask_server():
    app.run(host="127.0.0.1", port=5000)

@app.route("/test", methods=["GET"])
def testIntegration ():
    return jsonify({"status": "Recebido!!!"}), 200

@app.route("/getState/<deviceId>", methods=["GET"])
def getStateDevice(deviceId):

    print(deviceId)
    resposta = communication.getActualState(deviceId)
    if resposta is None:
        return jsonify({"message":"Erro ao se comunicar com o dispositivo"}), 500
    device ={
        "name": resposta.getName(),
        "speed": resposta.getSpeed(),
        "consumption": resposta.getConsumption()
    }
    return jsonify(device), 200

@app.route("/devices", methods=["GET"])
def getDevices():
    devicesList = list(communication.devices.keys())
    return jsonify({"devices":devicesList}), 200

@app.route("/update", methods=["POST"])
def updateDevice():
    data = request.get_json()

    resposta = communication.updateState(data.get("deviceName"), data.get("newSpeed"))
    if isinstance(resposta, str):
        return jsonify({"message":resposta}), 404
    elif resposta is None:
        return jsonify({"message":"Erro ao se comunicar com o dispositivo"}), 500
    device ={
        "name": resposta.getName(),
        "speed": resposta.getSpeed(),
        "consumption": resposta.getConsumption()
    }
    return jsonify(device), 200