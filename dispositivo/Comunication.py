import socket

class Comunication:
    #Classe para a comunicação com broker
    def __init__(self, device, brokerAddress):
        self.device = device
        self.brokerAddress = brokerAddress


    #Manda primeira mensagem para identificação do dispositivo
    def sendFirtsMessage(self, address, port, ip_address, portAp):
        message = self.addOnBroker()
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_server.bind((ip_address, portAp))
    
        socket_server.settimeout(5)
        print(address, port)

        socket_server.sendto(message.encode('utf-8'), (address, port))

        try:
            resposta, address = socket_server.recvfrom(1024)
            print("Resposta do dispositivo:", resposta.decode('utf-8'))

        except socket.timeout:
            raise
        finally:
                # Fecha o socket quando a thread terminar
                socket_server.close()

    #Tratamento da mensagem quando é recebida
    def receiveMessage(self, message, address):
        message = message.split(';')
        command = message[0]

        #Valida qual o comando para responder adequadamente
        if command == "get":
            response = self.getActualState(address)
        #Tenta atualizar, se não conseguir, manda um 400    
        elif command == "update":
            try:                
                response = self.updateState(address, message[3])
            except Exception as e:
                erro_mensagem = str(e) 
                print(f"Erro ao tentar atualizar: {erro_mensagem}")
                response = f"400;{self.device.getId()};{address};0;{erro_mensagem}"  
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.sendto(response.encode('utf-8'), (address[0], address[1]))
        server_socket.close()



    #Monta mensagem solicitando a adição no broker
    def addOnBroker(self):
        return f"add;{self.device.getId()};{self.brokerAddress};0"
    

    #Monta resposta da solicitação de estado atual    
    def getActualState(self, requestAddress):
        return f"200;{self.device.getId()};{requestAddress};{self.device.getInformation()}"
    
    #Atualiza o estado do dispositivo
    def updateState(self, requestAddress, speed):
        self.device.setSpeed(speed)
        return f"200;{self.device.getId()};{requestAddress};{self.device.getInformation()}"
