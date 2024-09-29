import time

# Constants
# Oder size
BYTE = 1
HALFBYT = 2
# Cursor direction
INCREMENT = 1
DECREMENT = 2
# Scrolling screen
SCROLLING_SCRREN = 1
STATIC_SCREEN = 2
# Cursor and blink
CURSOR_AND_BLINK = 1
CURSOR_NO_BLINK = 2
NO_CURSOR_NO_BLINK = 3
# LINES and DOTS
LINES1 = 1
LINES2 = 2
DOTS5x8 = 1
DOTS5x10 = 2
# Screen status
SCREEN_BUSY = 1
SCREEN_READY = 0
# Display control
DISPLAY_ON = 1
DISPLAY_OFF = 0

# Instuction code
CLEAR_DISPLAY = 0x01
RETURN_HOME = 0x02
ENTRY_MODE_SET = 0x04
DISPLAY_CONTROL = 0x08
CURSOR_DISPLAY_SHIFT = 0x10
FUNCTION_SET = 0x20
SET_CGRAM_ADDRESS = 0x40
SET_DDRAM_ADDRESS = 0x80


class LCDScreen:
    def __init__(self,
                 mode=BYTE,
                 lines=LINES2,
                 dots=DOTS5x8,
                 cursorMode=NO_CURSOR_NO_BLINK,
                 cursorDirection=INCREMENT,
                 scroll=STATIC_SCREEN):
        self.mode = mode
        self.lines = lines
        self.dots = dots
        self.cursorMode = cursorMode
        self.cursorDirection = cursorDirection
        self.scroll = scroll

    def setPinEnable(self, pin):
        self.pinEnable = pin

    def setPinRS(self, pin):
        self.pinRS = pin

    def setPinRW(self, pin):
        self.pinRW = pin

    def sendInstuction(self, instruction):
        while self.readBusyFlag() == SCREEN_BUSY:
            time.sleep(0.001)

    def sendChar(self, char):
        pass

    def sendString(self, string):
        pass

    def readBusyFlag(self):        
        return SCREEN_READY

    def readChar(self):
        pass

    def clearDisplay(self):
        self.sendInstuction(CLEAR_DISPLAY)

    def returnHome(self):
        self.sendInstuction(RETURN_HOME)

    def entryModeSet(self, direction=0, shift=0):
        if direction == 0:
            direction = self.cursorDirection
        if shift == 0:
            shift = self.scroll

        self.sendInstuction(ENTRY_MODE_SET | (direction << 1) | shift)

    def displayControl(self, display=DISPLAY_ON, cursorMode=0):
        if cursorMode == 0:
            cursorMode = self.cursorMode

        if cursorMode == CURSOR_AND_BLINK:
            cursor = 0
            blink = 0
        elif cursorMode == CURSOR_NO_BLINK:
            cursor = 1
            blink = 0
        else:
            cursor = 1
            blink = 1
        instruction = DISPLAY_CONTROL | (display << 2) | (cursor << 1) | blink
        self.sendInstuction(instruction)

    def cursorDisplayShift(self, direction=0, scroll=0):
        if direction == 0:
            direction = self.cursorDirection
        if scroll == 0:
            display = self.scroll

        self.sendInstuction(CURSOR_DISPLAY_SHIFT | (direction << 2) | display)

    def functionSet(self, DataLength=0, lines=0, dots=0):
        if DataLength == 0:
            self.DataLength = self.mode
        if lines == 0:
            lines = self.lines
        if dots == 0:
            dots = self.dots

        instruction = FUNCTION_SET | (self.DataLength << 4) | (lines << 3)
        instruction = instruction | (dots << 2)
        self.sendInstuction(instruction)

    def setCGRAMAddress(self, address):
        self.sendInstuction(SET_CGRAM_ADDRESS | address)

    def setDDRAMAddress(self, address):
        self.sendInstuction(SET_DDRAM_ADDRESS | address)
