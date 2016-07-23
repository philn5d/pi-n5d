import RPi.GPIO as g
import PiOutPin as p

class PiBCMHeader:    
    def __init__(self):
        g.setmode(g.BCM)
        self.pins = {}

    def initBoard(self):
        g.Cleanup()
        
    def addOutputPin(self, number):
        self.pins[number] = p.PiOutPin(number)
        return self.pins.get(number)

