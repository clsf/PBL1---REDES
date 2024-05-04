import socket
import errno
import threading
from Communication import communication
from CommunicationWithApplication import start_flask_server  
import os


#Define o IP como '0.0.0.0', verifica se a porta para comunicação com device a aplicação foram enviadas
#como variaveis de ambiente, se não, utilizam padrão 
ip_address = '0.0.0.0'
try:
    portToDevice = int(os.getenv("PORT_TO_DEVICE"))
except Exception:
    print("Porta para o device não estabelcida, usando default:5433")
    portToDevice = 5433

try:    
    portToApp = int(os.getenv("PORT_TO_APP"))
except Exception:
    print("Porta para aplicação não estabelecida, usando default: 5000")
    portToApp=5000

#Configura o socket para receber as mensagens via UDP do dispositivo
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((ip_address, portToDevice))

server_socket.setblocking(False)

bound_address = server_socket.getsockname()

print("Socket está bindado a:", bound_address)

#Inicia o flask para comunicação com a aplicação em uma thread 
flask_thread = threading.Thread(target=start_flask_server, args=(portToApp, ))
flask_thread.daemon = True  
flask_thread.start()

print("Servidor Flask iniciado. Aguardando requisições...")
##Começa a receber as mensagens do dispositivo
while True:

    try:
        data, client_address = server_socket.recvfrom(1024)        
        print("Mensage recived")
        #Quando recebe uma mensagem, abre uma thread para o processamento da mensagem
        threadReceiveMessage = threading.Thread(target=communication.receiveMessage, args=(data.decode(), client_address,))
        threadReceiveMessage.start()


    except socket.error as e:
       
        if e.errno == errno.EWOULDBLOCK:
            pass
        else:
            print("Erro:", e)