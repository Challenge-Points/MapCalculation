import json, math, sympy
from math import acos, pi

def modToRaw(score, mods):
    ######################################
    # List of mods                       #
    # NF, NO, NB, SS, IF, BE, DA, FS, GN #
    ######################################
    amount = len(mods)
    a = 0
    mod = 1
    while a < amount:
        if mods[a] == 'NF':
            mod = mod - 0.5
        elif mods[a] == 'NO':
            mod = mod - 0.95
        elif mods[a] == 'NB':
            mod = mod - 0.90
        elif mods[a] == 'SS':
            mod = mod - 0.70
        elif mods[a] == 'IF':
            mod = mod + 0.16
        elif mods[a] == 'BE':
            mod = mod + 0.10
        elif mods[a] == 'DA':
            mod = mod + 0.07
        elif mods[a] == 'FS':
            mod = mod + 0.08
        elif mods[a] == 'GN':
            mod = mod + 0.11
        a = a + 1
    score = score * mod
    round(score, 0)
    return score

def scoreToAcc(notes, score):
    notes = notes - 14
    a = notes*920
    b = a+4830
    acc = round((score/b)*100, 4)
    return acc

def getScore(userID, acc, weight):
    f = (-0.0000000089146*acc**5)+(0.0000036255812*acc**4)+(-0.0004061889074*acc**3)+(0.003306769423*acc**2)+(1.9970958028178*acc)
    if (0 <= acc <= 135):
        g = (2*acc)-(f)
        h = g/100
    else:
        h = 0
    cp = round(weight*h, 2)
    return cp

def getLenght(x1, x2, y1, y2):
    c = math.hypot(x2 - x1, y2 - y1)
    return c

def getNotes(file):
    lines = open(file, "r").read().split('\"_notes\":[')
    notes = str(lines[1]).split('],"_obstacles":')
    return notes[0]

def createChunks(notes):
    notesarray = str(notes).split(',')
    ###############
    # Beat 0 dict #
    ###############
    a = 0   #While loop counter
    d = 0   #Begin of chunk
    b = 2   #End of chunk
    e = 0   #Chunk Naming
    chunk = []
    chunkdict = {}
    while a < len(notesarray):
        c = str(notesarray[a]).split(':')
        if c[0] == '{"_time"':
            if float(c[1]) >= b:
                chunkdict[f'chunk{e}'] = chunk
                chunk = []
                d = d + 2
                b = b + 2
                e = e + 1
            if float(c[1]) >= d and float(c[1]) <= b:
                chunk.append(f'{notesarray[a]},{notesarray[a+1]},{notesarray[a+2]},{notesarray[a+3]},{notesarray[a+4]}')
        a = a + 1
    with open("dict0.json", "w") as outfile:  
        json.dump(chunkdict, outfile)
    ###############
    # Beat 1 dict #
    ###############
    a = 0   #While loop counter
    d = 1   #Begin of chunk
    b = 3   #End of chunk
    e = 0   #Chunk Naming
    chunk = []
    chunkdict = {}
    while a < len(notesarray):
        c = str(notesarray[a]).split(':')
        if c[0] == '{"_time"':
            if float(c[1]) >= b:
                chunkdict[f'chunk{e}'] = chunk
                chunk = []
                d = d + 2
                b = b + 2
                e = e + 1
            if float(c[1]) >= d and float(c[1]) <= b:
                chunk.append(f'{notesarray[a]},{notesarray[a+1]},{notesarray[a+2]},{notesarray[a+3]},{notesarray[a+4]}')
        a = a + 1
    with open("dict1.json", "w") as outfile:  
        json.dump(chunkdict, outfile)

def notesToAngle(CutDir1, x1, y1, CutDir2, x2, y2):
    x3 = 0
    y3 = 0
    x4 = 0
    y4 = 0
    if CutDir1 == 0:
        x3 = x1
        y3 = y1 + 1
    elif CutDir1 == 1:
        x3 = x1
        y3 = y1 - 1
    elif CutDir1 == 2:
        x3 = x1 - 1
        y3 = y1
    elif CutDir1 == 3:
        x3 = x1 + 1
        y3 = y1
    elif CutDir1 == 4:
        x3 = x1 - 1
        y3 = y1 + 1
    elif CutDir1 == 5:
        x3 = x1 + 1
        y3 = y1 + 1
    elif CutDir1 == 6:
        x3 = x1 - 1
        y3 = y1 - 1
    elif CutDir1 == 7:
        x3 = x1 + 1
        y3 = y1 - 1
    elif CutDir1 == 8:
        x3 = x1 + 1
        y3 = y1 + 1
    elif CutDir2 == 0:
        x4 = x2
        y4 = y2 + 1
    elif CutDir2 == 1:
        x4 = x2
        y4 = y2 - 1
    elif CutDir2 == 2:
        x4 = x2 - 1
        y4 = y2
    elif CutDir2 == 3:
        x4 = x2 + 1
        y4 = y2
    elif CutDir2 == 4:
        x4 = x2 - 1
        y4 = y2 + 1
    elif CutDir2 == 5:
        x4 = x2 + 1
        y4 = y2 + 1
    elif CutDir2 == 6:
        x4 = x2 - 1
        y4 = y2 - 1
    elif CutDir2 == 7:
        x4 = x2 + 1
        y4 = y2 - 1
    elif CutDir2 == 8:
        x4 = x2 + 1
        y4 = y2 + 1
    try:
        a = sympy.Line((x1, y1), (x3, y3))
        b = sympy.Line((x2, y2), (x4, y4))
        angle = a.smallest_angle_between(b)
    except ValueError:
        angle = 0
    return angle