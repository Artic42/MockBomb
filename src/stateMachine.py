from src import hardware as HW
from src import apiCalls


# Steate codes
STATE_INIT = 0
STATE_READY = 1
STATE_TIMER = 2
STATE_ARMED = 10
STATE_DEFUSE1 = 11
STATE_DEFUSED = 12
STATE_EXPLODED = 20


class StateMachine:
    def __init__(self):
        self.state: int = STATE_INIT

    def runStateMachine(self) -> None:
        if self.state == STATE_INIT:
            self.stateInit()
        elif self.state == STATE_READY:
            self.stateReady()
        elif self.state == STATE_TIMER:
            self.stateTimer()
        elif self.state == STATE_ARMED:
            self.stateArmed()
        elif self.state == STATE_DEFUSE1:
            self.stateDefuse1()
        elif self.state == STATE_DEFUSED:
            self.stateDefused()
        elif self.state == STATE_EXPLODED:
            self.stateExploded()
        else:
            self.state = STATE_INIT
        if self.timerRunning:
            self.timer()

    def timer(self) -> None:
        self.timeRemainingSeconds = self.timeRemaining // 10
        timeMinutes = self.timeRemainingSeconds // 60
        timeSeconds = self.timeRemainingSeconds % 60
        timeMinutesFirstDigit = timeMinutes // 10
        timeMinutesSecondDigit = timeMinutes % 10
        timeSecondsFirstDigit = timeSeconds // 10
        timeSecondsSecondDigit = timeSeconds % 10

        HW.screen.returnHome()
        HW.screen.clearDisplay()
        HW.screen.sendString("BOMB ARMED")
        HW.screen.setDDRAMAddress(0x44)
        stringTime = ""
        stringTime += str(timeMinutesFirstDigit)
        stringTime += str(timeMinutesSecondDigit)
        stringTime += ":"
        stringTime += str(timeSecondsFirstDigit)
        stringTime += str(timeSecondsSecondDigit)
        HW.screen.sendString(stringTime)
        self.timeRemaining -= 1
        if self.timeRemaining <= 0:
            apiCalls.sendExplodedMessage()
            self.state = STATE_EXPLODED

    def getState(self) -> int:
        return self.state

    def stateInit(self) -> None:
        self.timeRemaining: int = 0
        self.timeSet: int = 5
        self.timerRunning: bool = False
        self.bombArmed: bool = False
        self.bombDefused: bool = False
        HW.screen.screenInit()
        self.state = STATE_READY

    def stateReady(self) -> None:
        HW.screen.clearDisplay()
        HW.screen.sendString("BOMB READY")
        HW.screen.setDDRAMAddress(0x40)
        HW.screen.sendString("PRESS ARM")
        if HW.buttonEnter.isLOW():
            self.state = STATE_TIMER

    def stateTimer(self) -> None:
        timeMinutes = self.timeSet
        timeMinutesFirstDigit = timeMinutes // 10
        timeMinutesSecondDigit = timeMinutes % 10

        HW.screen.returnHome()
        HW.screen.clearDisplay()
        HW.screen.sendString("SET TIMER")
        HW.screen.setDDRAMAddress(0x40)
        stringTime = "MINUTES: "
        stringTime += str(timeMinutesFirstDigit)
        stringTime += str(timeMinutesSecondDigit)
        HW.screen.sendString(stringTime)
        if HW.buttonDown.isLOW():
            self.timeSet -= 1
            if self.timeSet < 5:
                self.timeSet = 5
        elif HW.buttonUp.isLOW():
            self.timeSet += 1
            if self.timeSet > 30:
                self.timeSet = 30
        if HW.buttonBack.isLOW():
            self.state = STATE_READY
        while HW.buttonDown.isLOW():
            pass
        while HW.buttonDown.isLOW():
            pass
        while HW.buttonUp.isLOW():
            pass
        if HW.buttonEnter.isLOW():
            self.timeRemaining = self.timeSet * 600
            self.timerRunning = True
            apiCalls.sendArmedMessage()
            self.state = STATE_ARMED

    def stateArmed(self) -> None:
        self.timerRunning = True
        if HW.blueCable.isHIGH():
            self.state = STATE_DEFUSE1
        if HW.purpleCable.isHIGH():
            apiCalls.sendExplodedMessage()
            self.state = STATE_EXPLODED
        if HW.greenCable.isHIGH():
            apiCalls.sendExplodedMessage()
            self.state = STATE_EXPLODED

    def stateDefuse1(self) -> None:
        self.timerRunning = True
        if HW.purpleCable.isHIGH():
            apiCalls.sendDefusedMessage()
            self.state = STATE_DEFUSED
        if HW.greenCable.isHIGH():
            apiCalls.sendExplodedMessage()
            self.state = STATE_EXPLODED

    def stateDefused(self) -> None:
        self.timerRunning = False
        cableConnected = HW.purpleCable.isLOW()
        cableConnected = cableConnected and HW.greenCable.isLOW()
        cableConnected = cableConnected and HW.blueCable.isLOW()
        if cableConnected:
            self.state = STATE_READY
        HW.screen.clearDisplay()
        HW.screen.sendString("BOMB DEFUSED")

    def stateExploded(self) -> None:
        self.timerRunning = False
        HW.redLED.write(True)
        HW.screen.clearDisplay()
        HW.screen.sendString("BOMB EXPLODED")
        HW.screen.setDDRAMAddress(0x40)
        HW.screen.sendString("GAME OVER")
        while HW.buttonEnter.isHIGH():
            pass
        self.state = STATE_INIT
