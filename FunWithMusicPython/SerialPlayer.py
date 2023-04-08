

def playTone(freq, dur, punct, serial):
    freqCode = repr(freq)
    durCode = repr(dur)
    punctCode = repr(punct)
    toWrite = freqCode + "#" + durCode + '#' + punctCode + '#'
    toWrite = toWrite.encode()
    serial.write(toWrite)
    serial.flush()
    return serial.readline()