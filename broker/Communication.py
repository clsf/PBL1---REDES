import socket
#Classe responsável pelo tratamento da comunicação com o device
from DeviceResponse import DeviceResponse
class Communication:

    def __init__(self, devices):
        self.devices = devices

    #Adiciona o device ao dicionário de devices com seu ID como chave e seu endereço como valor
    def addDevice(self, name, address):
        self.devices[name] = address
        print(address)
        #Retorna resposta padrão em caso de sucesso "codigo;remetente;destinatario"
        return f"200;broker;{name}"
    

    #Metodo para tratamento da mensagem recebida pelo dispositivo
    def receiveMessage(self, message, address):
        message = message.split(';')
        command = message[0]

        #Verifica se o que está sendo recebido é uma mensagem de add, se não, retorna um erro 400
        if command=="add":
            response = self.addDevice(message[1],address)
        else:
            response = f"400;broker;{message[1]}"
        
        #Responde a mensagem recebida via UDP para quem enviou
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.sendto(response.encode('utf-8'), (address[0], address[1]))
        server_socket.close()
    
    #Pega o estado atual do dispositivo
    def getActualState(self, deviceName):
        #Monta amensagem que será enviado para o dispositivo 
        message = f"get;broker;{deviceName};0"
        address = self.devices[deviceName]
        
        #Configura o socket para TCP e tenta conectar no endereço do dispositivo
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.connect((address[0], address[1]))

        socket_server.sendall(message.encode('utf-8'))

        tcp_port = socket_server.getsockname()[1]

        socket_server.close()

        #Muda o socket para receber mensagem via UDP, assim esperando a resposta do dispositivo por 5s 
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
            
            #Constrói a mensagem de resposta para a aplicação que solicitou
            deviceResponse = DeviceResponse(deviceName, deviceInformation[0], deviceInformation[1])
            print(deviceResponse)
            return (deviceResponse)
        #Tratamento de possiveis erros
        except socket.timeout:
            print("Status:500 \nNão houve resposta")
            return None
        except Exception as e:
            print(f"Erro ao escutar por conexões TCP: {e}")
        finally:
                # Fecha o socket quando a thread terminar
                socket_server.close()
                
    #Atualiza o status do dispositivo
    def updateState(self, deviceName, newState):
        #Monta a mensagem que será enviada para o dispositivo
        message = f"update;broker;{deviceName};{newState}"
        address = self.devices[deviceName]

        #Manda o comando para o dispositivo via TCP
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.connect((address[0], address[1]))

            socket_server.sendall(message.encode('utf-8'))
        except Exception:
            return "Erro ao se conectar com dispositivo, solicitacao nao atendida."

        tcp_port = socket_server.getsockname()[1]

        socket_server.close()

        #Prepara o socket para receber a mensagem via UDP
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

#Instancia o objeto responsável pela comunicação com o dispositivo.
communication = Communication({})