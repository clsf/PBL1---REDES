class DeviceResponse:
    #Classe para definir os atributos que serão enviados para o dispositivo.
    def __init__(self, name, speed, consumption) -> None:
        self.name = name
        self.speed = speed
        self.consumption = consumption

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
    
    def getConsumption(self):
        return self.consumption