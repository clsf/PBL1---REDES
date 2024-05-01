from datetime import datetime

class Device:
    def __init__(self, speed, consumption, start, id):
        self.speed = speed
        self.consumption = consumption
        self.start = start
        self.id = id

    def setSpeed(self, speed):
        if(speed != self.speed):            
            if self.speed=="0" and speed !="0":
                self.start = datetime.now()
            elif(speed == "0"):
                self.start = 0
            self.speed = speed

    def getId(self):
        return self.id

    
    def getSpeed (self):
        return self.speed
    
    def setConsumption(self):
        if(self.start != 0):
            actualHour = datetime.now()
            difference = actualHour - self.start
            self.consumption = self.consumption + (0.1 * (difference.total_seconds()))


    def getConsuption(self):
        self.setConsumption()
        return self.consumption
    
    def getInformation(self):        
        return f"V:{self.speed},C:{self.getConsuption()}"