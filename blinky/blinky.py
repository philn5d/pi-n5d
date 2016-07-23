import RPi.GPIO as GPIO
import time
def go(SPEED = 1):
        PIN = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, 1)
        try:
                while True:
                        GPIO.output(PIN, 0)
                        time.sleep(SPEED)
                        GPIO.output(PIN, 1)
                        time.sleep(SPEED)
        except KeyboardInterrupt:
                GPIO.output(PIN, 1)
                GPIO.cleanup()
