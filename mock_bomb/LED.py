import RPi.GPIO as GPIO


class LED():
    def __init__(self, pin):
        self.pin = pin
        self.state = False
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = True

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.state = False

    def toggle(self):
        if self.state:
            self.off()
        else:
            self.on()
