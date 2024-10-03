import RPi.GPIO as GPIO
from src import pinout

from rpi_artic_lib.GPIO import input
from rpi_artic_lib.GPIO import output
from rpi_artic_lib import screenLCD


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
    global screen
    global greenCable
    global blueCable
    global purpleCable

    # Set the GPIO mode to BCM.
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Initialize the buttons and LEDs.
    buttonEnter = input.Input(pinout.BUTTONENTER_PIN)
    buttonUp = input.Input(pinout.BUTTONUP_PIN)
    buttonDown = input.Input(pinout.BUTTONDOWN_PIN)
    buttonBack = input.Input(pinout.BUTTONBACK_PIN)

    redLED = output.Output(pinout.REDLED_PIN)
    greenLED = output.Output(pinout.GREENLED_PIN)
    yellowLED = output.Output(pinout.YELLOWLED_PIN)

    greenCable = input.Input(pinout.CABLEGREEN_PIN)
    blueCable = input.Input(pinout.CABLEBLUE_PIN)
    purpleCable = input.Input(pinout.CABLEPURPLE_PIN)

    screen = screenLCD.LCDScreen(
        pinout.SCREENRS_PIN,
        pinout.SCREENRW_PIN,
        pinout.SCREENE_PIN,
        pinout.SCREEN_DATABUS,
    )
