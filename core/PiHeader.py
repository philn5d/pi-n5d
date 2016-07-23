import RPi.GPIO as g
import core as p

class PiBCMHeader:    
    def __init__(self):
        g.setmode(g.BCM)
        self.pins = {}

    def __del__(self):
        g.cleanup()
        
    def addOutputPin(self, number):
        self.pins[number] = p.PiOutPin(number)
        return self.pins.get(number)

