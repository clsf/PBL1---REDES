import socket
import errno
import time
from Device import Device
from Comunication import Comunication
import threading
import os

#Init comunication and device
device = Device("0",0,0,"device1")
comunication = Comunication(device, "('127.0.0.1', 5433)")


ip_address = '0.0.0.0'
print(ip_address)

brokerAddress = os.getenv("BROKER_ADDRESS")
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



firtsSend = False 

while (firtsSend == False):
    try:
        #Send the firts message of recognition
        comunication.sendFirtsMessage(brokerAddress, brokerPort, ip_address, port)
        firtsSend = True
    except socket.timeout:
        print("Timeout: não foi possível receber uma resposta do broker.")
        time.sleep(1)
        print("Tentando mais 1 vez")

#Init socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port))
server_socket.listen(1)

    
while True:
    try:
        conn, client_address = server_socket.accept()
        data = conn.recv(1024)

        threadReceiveMessage = threading.Thread(target=comunication.receiveMessage, args=(data.decode(), client_address,))
        threadReceiveMessage.start()
        
    except socket.error as e:
    # Se nenhum dado estiver disponível, ignore e continue
        if e.errno == errno.EWOULDBLOCK:
            pass
        else:
            # Se for outra exceção, imprima o erro ou lide com ele de acordo
            print("Erro:", e)

        
        

