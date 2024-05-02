import socket
from DeviceResponse import DeviceResponse
class Communication:

    def __init__(self, devices):
        self.devices = devices

    def addDevice(self, name, address):
        self.devices[name] = address
        print(address)
        return f"200;broker;{name}"
    

    def receiveMessage(self, message, address):
        message = message.split(';')
        command = message[0]

        if command=="add":
            response = self.addDevice(message[1],address)
        else:
            response = f"400;broker;{message[1]}"
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.sendto(response.encode('utf-8'), (address[0], address[1]))
        server_socket.close()
    
    
    def getActualState(self, deviceName):

        message = f"get;broker;{deviceName};0"
        address = self.devices[deviceName]
        
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.connect((address[0], address[1]))

        socket_server.sendall(message.encode('utf-8'))

        tcp_port = socket_server.getsockname()[1]

        socket_server.close()

        socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_server.bind(('0.0.0.0', tcp_port))
        socket_server.settimeout(5)

        try:
            resposta, address = socket_server.recvfrom(1024)
            print("Resposta do dispositivo:", resposta.decode('utf-8'))
            resposta = resposta.decode('utf-8').split(';')
            print(resposta)
            deviceName = resposta[1]
            deviceInformation = resposta[3].split(",")
            
            
            deviceResponse = DeviceResponse(deviceName, deviceInformation[0], deviceInformation[1])
            print(deviceResponse)
            return (deviceResponse)

        except socket.timeout:
            print("Status:500 \nNão houve resposta")
            return None
        except Exception as e:
            print(f"Erro ao escutar por conexões TCP: {e}")
        finally:
                # Fecha o socket quando a thread terminar
                socket_server.close()
                

    def updateState(self, deviceName, newState):

        message = f"update;broker;{deviceName};{newState}"
        address = self.devices[deviceName]
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.connect((address[0], address[1]))

            socket_server.sendall(message.encode('utf-8'))
        except Exception:
            return "Erro ao se conectar com dispositivo, solicitacao nao atendida."

        tcp_port = socket_server.getsockname()[1]

        socket_server.close()

        socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_server.bind(('0.0.0.0', tcp_port))
        socket_server.settimeout(5)
        try:
            resposta, address = socket_server.recvfrom(1024)
            print("Resposta do dispositivo:", resposta.decode('utf-8'))
            resposta = resposta.decode('utf-8').split(';')
            deviceName = resposta[1]
            deviceInformation = resposta[3].split(",")
            deviceResponse = DeviceResponse(deviceName, deviceInformation[0], deviceInformation[1])
            return (deviceResponse)
            
        except socket.timeout:
            return None
        finally:
                # Fecha o socket quando a thread terminar
                socket_server.close()

communication = Communication({})