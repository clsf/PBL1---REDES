import socket
import errno
import time
from Device import Device
from Comunication import Comunication
import threading
import os

#Metodo para permitir entradas via terminal
def getInformationByTerminal(device):
    while True:
        print("\nInformação atual:" + device.getInformation())
        newSpeed = input("\nDigite o valor da velocidade para o dispositivo:")
        device.setSpeed(newSpeed)


#Pega as variaveis de ambiente, se não tiver, é configurado as default 
ip_address = '0.0.0.0'
print(ip_address)

brokerAddress = os.getenv("BROKER_ADDRESS")
deviceName = os.getenv("DEVICE_NAME")
try:
    brokerPort = int(os.getenv("BROKER_PORT"))
except Exception:
    print("Porta do broker não estabelecida, usando default: 5433")
    brokerPort=5433

try:
    port = int(os.getenv("PORT"))
except Exception:
    port = 5432
    print("Porta do serviço não estabelecida, usando default: 5432")

if not brokerAddress:
    brokerAddress ='127.0.0.1'

if not deviceName: deviceName="device"

#Init comunication and device
device = Device("0",0,0,deviceName)
comunication = Comunication(device, "('127.0.0.1', 5433)")

#Manda a primeira mensagem pro broker, o dispositivo só funciona depois do recebimento de confirmação do broker
firtsSend = False 

while (firtsSend == False):
    try:
        #Envia a primeira mensagem
        comunication.sendFirtsMessage(brokerAddress, brokerPort, ip_address, port)
        firtsSend = True
    except socket.timeout:
        print("Timeout: não foi possível receber uma resposta do broker.")
        time.sleep(1)
        print("Tentando mais 1 vez")

#Após receber mensagem de sucesso, inicia a captura de solicitações via terminal
threadTerminal = threading.Thread(target=getInformationByTerminal, args=(device, ))
threadTerminal.start()
#Init socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port))
server_socket.listen(1)

#Espera mensagens do broker via UDP    
while True:
    try:
        conn, client_address = server_socket.accept()
        data = conn.recv(1024)

        #Inicia uma thread para o tratamento da mensagem
        threadReceiveMessage = threading.Thread(target=comunication.receiveMessage, args=(data.decode(), client_address,))
        threadReceiveMessage.start()
        
    except socket.error as e:
    # Se nenhum dado estiver disponível, ignore e continue
        if e.errno == errno.EWOULDBLOCK:
            pass
        else:
            # Se for outra exceção, imprima o erro ou lide com ele de acordo
            print("Erro:", e)

        
        

