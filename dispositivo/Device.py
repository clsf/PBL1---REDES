from datetime import datetime

class Device:
    #Classe responsável pela construção do objeto dispositivo
    def __init__(self, speed, consumption, start, id):
        self.speed = speed
        self.consumption = consumption
        self.start = start
        self.id = id

    #Configura a velocidade, se o dispositivo estava desligado e foi para o status de ativo, consumo é ativado
    #Se o dispositivo estava ligado e foi para o estado de desligado, consumo é desativo
    def setSpeed(self, speed):
        if(speed != self.speed):            
            if self.speed=="0" and speed !="0":
                self.start = datetime.now()
            elif(speed == "0"):
                self.start = 0
            self.speed = speed

    #Pega o ID
    def getId(self):
        return self.id

    #Pega a velocidade
    def getSpeed (self):
        return self.speed
    
    #Configura o consumo com base no tempo dele ativo e o momento da requisição e soma com o que já estava antes
    def setConsumption(self):
        if(self.start != 0):
            actualHour = datetime.now()
            difference = actualHour - self.start
            self.consumption = self.consumption + (0.1 * (difference.total_seconds()))

    #Pega o consumo com base na atualização
    def getConsuption(self):
        self.setConsumption()
        return self.consumption
    
    #Pega informação do dispositivo, como velocidade e consumo
    def getInformation(self):        
        return f"V:{self.speed},C:{self.getConsuption()}"