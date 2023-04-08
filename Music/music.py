import serial
from noteLookup import Notes as NOTEKEY
import Model
from Model import *

Model.DEBUG = DEBUG =  True
SERIAL_MODE = False

if SERIAL_MODE:
    SER = serial.Serial("COM4", 9600, timeout=None)
    SER.timeout = None

FILE_OVERRIDE = "Test"

def openFile():
    if FILE_OVERRIDE == "":
        name = input("What to play?" + "\n")
    else:
        name = FILE_OVERRIDE
    sheetDir = "Music\\Sheets\\"+name+".custommusic"
    return open(sheetDir)

try:
    sheet = openFile()
except FileNotFoundError:
    sheet = openFile()


if SERIAL_MODE: print(SER.readline())

PIECE = Piece(NOTEKEY)
PIECE.decodeSheet(sheet)

#print(PIECE.sheet)

if SERIAL_MODE:
    PIECE.playOnSerial(SER)
    SER.close()
else:  
    PIECE.playDigital()
