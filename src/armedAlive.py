from src import stateMachine as SM
from src import apiCalls


class APIArmedAlive:
    def __init__(self):
        self.counter: int = 0

    def getArmedAlive(self, state: int) -> bool:
        self.counter += 1
        if self.counter > 49:
            self.counter = 0
            if state == SM.STATE_ARMED:
                armed = True
            elif state == SM.STATE_DEFUSE1:
                armed = True
            elif state == SM.STATE_DEFUSED:
                armed = True
            else:
                armed = False
            if armed:
                apiCalls.sendAliveMessage()
