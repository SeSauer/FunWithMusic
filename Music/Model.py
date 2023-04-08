import SinePlayer, SerialPlayer


DEBUG = False

class Note():
    def __init__(self, freq, dur, punct = 0):
        self.freq = freq
        self.dur = dur
        self.punct = punct

    def __init__(self, sheetstring, noteKey):
        self.decodeString(sheetstring, noteKey)

    def decodeString(self, string, noteKey):
        literals = string.split()
        self.tone = literals[0].upper()
        self.invDur = float(literals[1])
        self.freq = noteKey[self.tone]
        self.punct = 0
        if len(literals) > 2:
            if "-s" in literals[2:]:
                self.punct = 1
            if "-l" in literals[2:]:
                self.punct = -1
            if "-p" in literals[2:]:
                self.invDur = self.invDur * (2 / 3)
            

    def writeToSerial(self, serial, wholeDur):
        dur = repr(int(wholeDur / self.invDur)) if not hasattr(self, "dur") else repr(int(self.dur))
        out = SerialPlayer.playTone(self.freq, dur, self.punct, serial)
        if DEBUG: print(self)
        if DEBUG : print(out)
    
    def __repr__(self) -> str:
        return f"({self.freq}:{self.invDur})"

    def playDigital(self, wholeDur):
        freq = int(self.freq)
        dur = int(wholeDur / self.invDur) if not hasattr(self, "dur") else int(self.dur)
        print(f"({freq}:{dur})")
        SinePlayer.playTone(freq, dur, self.punct)



class Piece():
    def __init__(self, noteKey):
        self.sheet : list[Note] = []
        self.wholeDur = 0
        self.noteKey = noteKey
    
    def addNote(self, note:Note):
        self.sheet.append(note)

    def decodeSheet(self, sheet):
        lines: list[str] = sheet.readlines()
        returnPoint = 1
        self.wholeDur = int(lines[0])
        i = 1
        while i < len(lines):
            line = lines[i].strip("\n ")
            if line.strip() == "" : continue
            if line[0] == '#': pass
            elif line == self.noteKey["RETURN"]: returnPoint = i
            elif line == self.noteKey["REPEAT"]: 
                lines.pop(i)
                i = returnPoint - 1
            else:
                n = Note(line, self.noteKey)
                self.addNote(n)
                #print(n)
            if DEBUG: print(i)
            i += 1        

    def playOnSerial(self, serial):
        for note in self.sheet:
            x = note.writeToSerial(serial, self.wholeDur)
            if DEBUG: print(x)

    def playDigital(self):
        for note in self.sheet:
            note.playDigital(self.wholeDur)