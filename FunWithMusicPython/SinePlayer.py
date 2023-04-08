from pysine import sine
import time

def playTone(freq = 440, dur = 1000, punct = 0):
        dif = calcDif(dur, punct)
        actDur = (dur - dif) / 1000
        sine(frequency=freq, duration = actDur)
        time.sleep(dif / 1000)  



def calcDif(dur: int, punct : int):
        if punct == 0: return min(100, dur * 0.1)
        if punct < 0 : return 0
        if punct > 0: return max(dur - 80, 0)

if __name__ == "__main__":
        playTone(392, 225)