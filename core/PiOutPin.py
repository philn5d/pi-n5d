import RPi.GPIO as g

class PiOutPin:

    def __init__(self, number):
        g.setup(number, g.OUT)
        self.number = number

    def pullUp(self):
        g.output(self.number, 1)

    def pullDown(self):
        g.output(self.number, 0)
