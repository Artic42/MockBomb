# Description: This is a mock bomb that will be used
# to test the bomb defusal program.
import time
from mock_bomb import hardware as HW
import articlib.articFileUtils as fileUtils


def main():
    HW.HWInit()
    while not fileUtils.fileExists("/home/artic/stop"):
        if HW.buttonEnter.isPressed():
            HW.redLED.on()
            HW.greenLED.off()
            HW.yellowLED.off()
        elif HW.buttonUp.isPressed():
            HW.redLED.off()
            HW.greenLED.on()
            HW.yellowLED.off()
        elif HW.buttonDown.isPressed():
            HW.redLED.off()
            HW.greenLED.off()
            HW.yellowLED.on()
        elif HW.buttonBack.isPressed():
            HW.redLED.off()
            HW.greenLED.off()
            HW.yellowLED.off()
        time.sleep(0.1)
    fileUtils.deleteFile("/home/artic/stop")


if __name__ == "__main__":
    main()
