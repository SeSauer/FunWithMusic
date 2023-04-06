Anleitung zum umschreiben von noten in .custommusic dateien

1. Zeile: geschwindigkeit des Stücks, angegeben in der Länge einer Ganzen note (in ms)
    120bpm -> 2000 (hohe zahl = langsamer)

danach:

-jede zeile, die mit einem # beginnt, wird ignoriert (kommentare)
-groß- kleinschreibung wird generell ignoriert

Noten: 
    Noten-Zeilen sind aufgebaut durch

    -eine durch eine notenschlüsseldatei (zum beispiel den Standartnotenschlüssel) codierte frequenz
    -ein leerzeichen
    -eine länge 
         dargestellt als anteil der ganzen, also 4 für eine viertelnote, 8 für eine achtelnote etc

Der Standertnotenschlüssel:
    eine codierte Note im Standartnotenschlüssel besteht aus:
    -dem Notennamen (englisch) (aus c,d,e,f,g,a,b)
        -oder der pause (p oder -)
    -optional einem vorzeichen # oder b
    der oktavzahl von 1 - 7
        dabei ist 1 die tiefste oktave und 7 die höchste
        die standartoktave ("kleine oktave") hat dabei nummer 4 
            bei der standartoktave kann die zahl auch weggelassen werden

    Bsp:
        c       -codierung kleines C
        C4      -"
        c5      -codierung c'
        c#      -codierung kleines cis
        c#5     -codierung cis'
        bb3     -codierung großes b
        p       -pause

        f#5 2   -Noten-Zeile einer halben note fis'

Wiederholungszeichen
    im Standartnotenschlüssel :|
    
    der teil seit dem letzten return-point (oder dem anfang der stücks) wird wiederholt

    Return-zeichen |:
       markiert einen return-point

Annotationen
an eine noten-zeile kann optional (nach einem leerzeichen) eine annotation angefügt werden,
    welche den ton beeinflusst

    Bisher implementierte annotationen:
        -l  der ton wird gehalten, bis der nächste ton beginnt. für gebundene oder punktierte noten
        -s  verkürzt den ton (staccato)

Beispiele:

    Bsp1:   spielt die ersten 6 töne der c-dur tonleiter
    2000
    c 4
    d 4
    e 4
    f 4
    g 4
    a 4


    Bsp2:   spielt die ersen 5 töne der b-dur tonleiter
    2000
    bb3 4
    c 4
    #wrxtrf
    d 4
    eb 4
    f 4


    Bsp3:   wie Bsp2, aber zweimal und doppelt so schnell
    1000
    bb3 4
    c 4
    d 4
    eb 4
    f 4
    :|


    Bsp4 : dasselbe wie Bsp3
    2000
    |:
    bb3 8
    c 8
    d 8
    eb 8
    f 8
    :|


    Bsp5: dasselbe wie Bsp1, aber mit gebundendenen tönen
    2000
    c 4 -l
    d 4
    e 4 -l
    f 4
    g 4 -l
    a 4

    Bsp6: dasselbe wie bsp1, aber eine oktave höher
    2000
    c5 4 
    d5 4
    e5 4 
    f5 4
    g5 4 
    a5 4