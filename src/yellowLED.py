from src import hardware as HW


class yellowLED:
    def __init__(self):
        self.counter: int = 0

    def handleYellowLED(self) -> None:
        self.counter += 1
        if self.counter > 9:
            self.counter = 0
        if self.counter < 5:
            HW.yellowLED.write(True)
        else:
            HW.yellowLED.write(False)
