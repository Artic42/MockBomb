import RPi.GPIO as GPIO


class button():
    def __init__(self, pin, pull_up_down=GPIO.PUD_UP):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=pull_up_down)

    def isPressed(self):
        return not GPIO.input(self.pin)

    def isReleased(self):
        return GPIO.input(self.pin)


class cable(button):
    pass
