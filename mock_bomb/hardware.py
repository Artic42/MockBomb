import RPi.GPIO as GPIO
import mock_bomb.pinout as pinout
import mock_bomb.button as button
import mock_bomb.LED as LED


def HWInit():
    # Description: This function initializes the hardware
    # of the mock bomb.
    # Define instances of the button and LED classes.
    global buttonEnter
    global buttonUp
    global buttonDown
    global buttonBack
    global redLED
    global greenLED
    global yellowLED

    # Set the GPIO mode to BCM.
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Initialize the buttons and LEDs.
    buttonEnter = button.button(pinout.BUTTONENTER_PIN)
    buttonUp = button.button(pinout.BUTTONUP_PIN)
    buttonDown = button.button(pinout.BUTTONDOWN_PIN)
    buttonBack = button.button(pinout.BUTTONBACK_PIN)

    redLED = LED.LED(pinout.REDLED_PIN)
    greenLED = LED.LED(pinout.GREENLED_PIN)
    yellowLED = LED.LED(pinout.YELLOWLED_PIN)
