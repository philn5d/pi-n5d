if __name__ == "__main__" and __package__ is None:
    import sys, os.path as path
    
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import time
import core
class Blinky:
    def __init__(self, *pinNumbers):
        self.pinNumbers = pinNumbers
        self.header = core.PiBcmHeader()
        self.pins = {}
        for n in self.pinNumbers:
            self.pins[n] = self.header.addOutputPin(n)
    def __del__(self):
        self.header.close()

    def start(self, blinkSpeed, times):
        while (times > 0):
            for n in self.pins.values():
                n.pullUp()
                time.sleep(blinkSpeed)
                n.pullDown()
                times-=1
                blinkSpeed+=.01
        print("stopped")

