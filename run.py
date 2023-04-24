import time
import board
import digitalio

#Defining Outputs
led_test = digitalio.DigitalInOut(board.GP28)
led_test.direction = digitalio.Direction.OUTPUT

en_81 = digitalio.DigitalInOut(board.GP0)
en_81.direction = digitalio.Direction.OUTPUT
A0_81 = digitalio.DigitalInOut(board.GP1)
A0_81.direction = digitalio.Direction.OUTPUT
A1_81 = digitalio.DigitalInOut(board.GP2)
A1_81.direction = digitalio.Direction.OUTPUT

en_91 = digitalio.DigitalInOut(board.GP3)
en_91.direction = digitalio.Direction.OUTPUT
A0_91 = digitalio.DigitalInOut(board.GP4)
A0_91.direction = digitalio.Direction.OUTPUT
A1_91 = digitalio.DigitalInOut(board.GP5)
A1_91.direction = digitalio.Direction.OUTPUT

en_92 = digitalio.DigitalInOut(board.GP6)
en_92.direction = digitalio.Direction.OUTPUT
A0_92 = digitalio.DigitalInOut(board.GP7)
A0_92.direction = digitalio.Direction.OUTPUT
A1_92 = digitalio.DigitalInOut(board.GP8)
A1_92.direction = digitalio.Direction.OUTPUT

en_93 = digitalio.DigitalInOut(board.GP9)
en_93.direction = digitalio.Direction.OUTPUT
A0_93 = digitalio.DigitalInOut(board.GP10)
A0_93.direction = digitalio.Direction.OUTPUT
A1_93 = digitalio.DigitalInOut(board.GP11)
A1_93.direction = digitalio.Direction.OUTPUT

en_94 = digitalio.DigitalInOut(board.GP16)
en_94.direction = digitalio.Direction.OUTPUT
A0_94 = digitalio.DigitalInOut(board.GP17)
A0_94.direction = digitalio.Direction.OUTPUT
A1_94 = digitalio.DigitalInOut(board.GP18)
A1_94.direction = digitalio.Direction.OUTPUT

en_82 = digitalio.DigitalInOut(board.GP19)
en_82.direction = digitalio.Direction.OUTPUT
A0_82 = digitalio.DigitalInOut(board.GP20)
A0_82.direction = digitalio.Direction.OUTPUT
A1_82 = digitalio.DigitalInOut(board.GP21)
A1_82.direction = digitalio.Direction.OUTPUT


#Creating Functions
def ledTestOn():
    led_test.value = True

def ledTestOff():
    led_test.value = False
'-------------------------'
def S_reset():
    en_81.value = False
    A0_81.value = False
    A1_81.value = False

    en_91.value = False
    A0_91.value = False
    A1_91.value = False

    en_92.value = False
    A0_92.value = False
    A1_92.value = False

    en_93.value = False
    A0_93.value = False
    A1_93.value = False

    en_94.value = False
    A0_94.value = False
    A1_94.value = False

    en_82.value = False
    A0_82.value = False
    A1_82.value = False
'-------------------------'
'''
def S_test():
    en_81.value = True
    A0_81.value = True
    A1_81.value = True

    en_91.value = True
    A0_91.value = True
    A1_91.value = True

    en_92.value = True
    A0_92.value = True
    A1_92.value = True
'''
'-------------------------'
'-------------------------'
def S1_81on():
    en_81.value = True
    A0_81.value = False
    A1_81.value = False

def S2_81on():
    en_81.value = True
    A0_81.value = True
    A1_81.value = False

def S3_81on():
    en_81.value = True
    A0_81.value = False
    A1_81.value = True

def S4_81on():
    en_81.value = True
    A0_81.value = True
    A1_81.value = True
'-------------------------'
'-------------------------'
def S1_91on():
    en_91.value = True
    A0_91.value = False
    A1_91.value = False

def S2_91on():
    en_91.value = True
    A0_91.value = True
    A1_91.value = False

def S3_91on():
    en_91.value = True
    A0_91.value = False
    A1_91.value = True

def S4_91on():
    en_91.value = True
    A0_91.value = True
    A1_91.value = True
'-------------------------'
'-------------------------'
def S1_92on():
    en_92.value = True
    A0_92.value = False
    A1_92.value = False

def S2_92on():
    en_92.value = True
    A0_92.value = True
    A1_92.value = False

def S3_92on():
    en_92.value = True
    A0_92.value = False
    A1_92.value = True

def S4_92on():
    en_92.value = True
    A0_92.value = True
    A1_92.value = True
'-------------------------'
'-------------------------'
def S1_93on():
    en_93.value = True
    A0_93.value = False
    A1_93.value = False

def S2_93on():
    en_93.value = True
    A0_93.value = True
    A1_93.value = False

def S3_93on():
    en_93.value = True
    A0_93.value = False
    A1_93.value = True

def S4_93on():
    en_93.value = True
    A0_93.value = True
    A1_93.value = True
'-------------------------'
'-------------------------'
def S1_94on():
    en_94.value = True
    A0_94.value = False
    A1_94.value = False

def S2_94on():
    en_94.value = True
    A0_94.value = True
    A1_94.value = False

def S3_94on():
    en_94.value = True
    A0_94.value = False
    A1_94.value = True

def S4_94on():
    en_94.value = True
    A0_94.value = True
    A1_94.value = True
'-------------------------'
'-------------------------'
def S1_82on():
    en_82.value = True
    A0_82.value = False
    A1_82.value = False

def S2_82on():
    en_82.value = True
    A0_82.value = True
    A1_82.value = False

def S3_82on():
    en_82.value = True
    A0_82.value = False
    A1_82.value = True

def S4_82on():
    en_82.value = True
    A0_82.value = True
    A1_82.value = True
'-------------------------'