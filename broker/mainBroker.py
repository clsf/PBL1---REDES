import socket
import errno
import threading
from Communication import communication
from CommunicationWithApplication import start_flask_server  
import os



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

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Servidor escutando na porta {portToApp}...")
server_socket.bind((ip_address, portToDevice))

server_socket.setblocking(False)

bound_address = server_socket.getsockname()

print("Socket está bindado a:", bound_address)


flask_thread = threading.Thread(target=start_flask_server, args=(portToApp, ))
flask_thread.daemon = True  
flask_thread.start()

print("Servidor Flask iniciado. Aguardando requisições...")

while True:

    try:
        data, client_address = server_socket.recvfrom(1024)        
        print("Mensage recived")
        threadReceiveMessage = threading.Thread(target=communication.receiveMessage, args=(data.decode(), client_address,))
        threadReceiveMessage.start()


    except socket.error as e:
       
        if e.errno == errno.EWOULDBLOCK:
            pass
        else:
            print("Erro:", e)