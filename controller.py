import pyfirmata
port = 'COM7'
pin1 = 9
pin2 = 10
board = pyfirmata.Arduino(port)


def glow(val):
    if val == 0:
        board.digital[pin2].write(1)
        board.digital[pin1].write(0)
    elif val == 1:
        board.digital[pin1].write(1)
        board.digital[pin2].write(0)