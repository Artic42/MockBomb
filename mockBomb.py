# Description: This is a mock bomb that will be used
# to test the bomb defusal program.
import time
from src import hardware as HW
from src import stateMachine as SM
from src import APIArmedAlive
from src import yellowLED
import articlib.articFileUtils as fileUtils


def main():
    HW.HWInit()
    yellow = yellowLED.yellowLED()
    state = SM.StateMachine()
    alive = APIArmedAlive.APIArmedAlive()
    while not fileUtils.fileExists("/home/artic/stop"):
        state.runStateMachine()
        alive.getArmedAlive(state.getState())
        yellow.handleYellowLED()
        handleRedLED(state.getState())
        handleGreenLED(state.getState())
        time.sleep(0.1)
    fileUtils.deleteFile("/home/artic/stop")


def handleRedLED(state: int) -> None:
    if state == SM.STATE_EXPLODED:
        HW.redLED.write(True)
    else:
        HW.redLED.write(False)


def handleGreenLED(state: int) -> None:
    if state == SM.STATE_ARMED:
        HW.greenLED.write(True)
    elif state == SM.STATE_DEFUSE1:
        HW.greenLED.write(True)
    else:
        HW.greenLED.write(False)


if __name__ == "__main__":
    main()
