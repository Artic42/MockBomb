# Description: This is a mock bomb that will be used
# to test the bomb defusal program.
import time
from src import hardware as HW
import articlib.articFileUtils as fileUtils


def main():
    HW.HWInit()

    HW.screen.screenInit()
    HW.screen.clearDisplay()
    HW.screen.returnHome()
    HW.screen.sendString("Mock Bomb")
    while not fileUtils.fileExists("/home/artic/stop"):
        if HW.buttonEnter.isLOW():
            HW.redLED.setHIGH()
            HW.greenLED.setLOW()
            HW.yellowLED.setLOW()
        elif HW.buttonUp.isLOW():
            HW.redLED.setLOW()
            HW.greenLED.setHIGH()
            HW.yellowLED.setLOW()
        elif HW.buttonDown.isLOW():
            HW.redLED.setLOW()
            HW.greenLED.setLOW()
            HW.yellowLED.setHIGH()
        elif HW.buttonBack.isLOW():
            HW.redLED.setLOW()
            HW.greenLED.setLOW()
            HW.yellowLED.setLOW()
        time.sleep(0.1)
    fileUtils.deleteFile("/home/artic/stop")


if __name__ == "__main__":
    main()
