import RPi.GPIO as g
import core as p

class PiBcmHeader:
  def __init__(self):
    self.pins = {}
    g.setmode(g.BCM)
    
  def close(self):
    g.cleanup()
        
  def addOutputPin(self, number):
    self.pins[number] = p.PiOutPin(number)
    return self.pins.get(number)
			
  def __exit__(self):
    self.close()
