if __name__ == "__main__" and __package__ is None:
    import sys, os.path as path
    
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import time
import core
class Blinky:

    def __init__(self, *pinNumbers):
        self.header = core.PiBCMHeader()
        self.pins = {}
        for n in pinNumbers:
            self.pins[n] = self.header.addOutputPin(n)

    def start(self, blinkSpeed):
        self.keepBlinking = True
        while self.keepBlinking == True:
            for n in self.pins.values():
                n.pullUp()
                time.sleep(blinkSpeed)
                n.pullDown()
                time.sleep(blinkSpeed)
    def stop(self):
        self.keepBlinking = False

