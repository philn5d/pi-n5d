import time
import RPi.GPIO as g

def setup(mode, inputChannel, outputChannel):
    g.setmode(g.BCM)
    g.setup(inputChannel, g.IN, g.PUD_UP)
    g.setup(outputChannel, g.OUT)
    def toggle(channel):
        onOff = g.input(channel)
        g.output(outputChannel, onOff)
    g.add_event_detect(inputChannel, g.BOTH, toggle)

def cleanup():
    g.cleanup()
