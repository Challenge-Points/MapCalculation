import json
from functionlib import *
from math import pi, acos, sqrt
bpm = int(input('What is the BPM of the map? [Int]: '))
input('Please make sure the file you want to evaluate is in the same folder as this file and is called "song.dat"\n press enter to continue')

#Split song into chunks
createChunks(getNotes('song.dat'))
#Read json outputs of the chunk split into variables
with open('dict0.json') as json_file:
    dict0 = json.load(json_file)
with open('dict1.json') as json_file:
    dict1 = json.load(json_file)
#While loops to cycle through the dicts and collect all data needed
a = 0
NS = 0
while a < len(dict0):
    d = 0
    while True:
        try:
            b = str(dict0[f'chunk{a}'][d]).split(',')
            line = str(b[1]).split(':')[1]
            type = str(b[3]).split(':')[1]
            if type == '0':
                if line != '0' or line != '1':
                    NS = NS + 1
            elif type == '1':
                if line != '2' or line != '3':
                    NS = NS + 1
            d = d + 1
        except IndexError:
            d = 0
            break
    a = a + 1
a = 0
while a < len(dict1):
    d = 0
    while True:
        try:
            b = str(dict1[f'chunk{a}'][d]).split(',')
            line = str(b[1]).split(':')[1]
            type = str(b[3]).split(':')[1]
            if type == '0':
                if line != '0' or line != '1':
                    NS = NS + 1
            elif type == '1':
                if line != '2' or line != '3':
                    NS = NS + 1
            d = d + 1
        except IndexError:
            d = 0
            break
    a = a + 1
a = 0
lines1 = []
cutdir1 = []
time1 = []
MAXBPM = 0
while a < len(dict0):
    f = len(f'dict0[chunk{a}]')
    if MAXBPM < f:
        MAXBPM = f
    if dict0[f'chunk{a}'] != []:
        d = 0
        while True:
            try:
                e = str(dict0[f'chunk{a}'][d]).split(',')
                f = str(e[0]).split('{')[1]
                lines1.append(f'{a}~{e[1]}~{e[2]}')
                cutdir1.append(f'{a}~{e[4]}')
                time1.append(f'{a}~{f}~{e[3]}')
                d = d + 1
            except IndexError:
                d = 0
                break
    a = a + 1
a = 0
lines2 = []
cutdir2 = []
time2 = []
while a < len(dict1):
    f = len(f'dict0[chunk{a}]')
    if MAXBPM < f:
        MAXBPM = f
    if dict1[f'chunk{a}'] != []:
        d = 0
        while True:
            try:
                e = str(dict0[f'chunk{a}'][d]).split(',')
                lines2.append(f'{a}~{e[1]}~{e[2]}')
                cutdir2.append(f'{a}~{e[4]}')
                f = str(e[0]).split('{')[1]
                time2.append(f'{a}~{f}~{e[3]}')
                d = d + 1
            except IndexError:
                d = 0
                break
    a = a + 1
#Create dict with triangles
a = 0
b = 0
triangles1 = []
while a < len(lines1):
    try:
        g = str(lines1[a]).split('~')
        h = str(lines1[a+1]).split('~')
        if g[0] == h[0]:
            c = f'{g[1]}~{g[2]}'
            d = f'{h[1]}~{h[2]}'
            f = g[0]
            triangles1.append(f'{f}~{c}~{d}')
    except IndexError:
        break
    a = a + 1
    b = b + 2
a = 0
b = 0
triangles2 = []
while a < len(lines2):
    try:
        g = str(lines2[a]).split('~')
        h = str(lines2[a+1]).split('~')
        if g[0] == h[0]:
            c = f'{g[1]}~{g[2]}'
            d = f'{h[1]}~{h[2]}'
            f = g[0]
            triangles2.append(f'{f}~{c}~{d}')
    except IndexError:
        break
    a = a + 1
    b = b + 2
#From the triangle dicts get the lenght between the 2 points and add the Avg Swing Distance points to the point dict
a = 0
ASD = 0
while a < len(triangles1):
    try:
        b = str(triangles1[a]).split('~')
        c = int(str(b[1]).split(':')[1])
        d = int(str(b[2]).split(':')[1])
        e = int(str(b[3]).split(':')[1])
        f = int(str(b[4]).split(':')[1])
        ASD = ASD + getLenght(c, e, d, f)
    except IndexError:
        break
    a = a + 1
a = 0
while a < len(triangles2):
    try:
        b = str(triangles2[a]).split('~')
        c = int(str(b[1]).split(':')[1])
        d = int(str(b[2]).split(':')[1])
        e = int(str(b[3]).split(':')[1])
        f = int(str(b[4]).split(':')[1])
        ASD = ASD + getLenght(c, e, d, f)
    except IndexError:
        break
    a = a + 1
ASD = round(ASD, 2)
#Get coordiantes of the blocks and put them through the notesToAngle function
a = 0
AAC = 0
while a < len(lines1):
    try:
        b = str(lines1[a]).split('~')
        d = str(b[2]).split(':')
        b = str(b[1]).split(':')
        e = str(lines2[a]).split('~')
        f = str(e[2]).split(':')
        e = str(e[1]).split(':')
        c = str(str(cutdir1[a]).split(':')[1]).split('}')
        g = str(str(cutdir2[a]).split(':')[1]).split('}')
        angle = eval(str(notesToAngle(c[0], int(b[1]), int(d[1]), g[0],int(f[1]), int(e[1]))))*180/math.pi
        AAC = AAC + angle
    except IndexError:
        None
    a = a + 1
AAC = round(AAC/(ASD*0.2), 2)
#Get distance between notes per type
a = 0
ASS = 0
while a < (len(time1)-1):
    b = str(str(time1[a]).split(',')).split('~')
    c = str(str(time1[a+1]).split(',')).split('~')
    d = float(str(b[1]).split(':')[1])
    e = float(str(c[1]).split(':')[1])
    ASS = ASS + (e - d)
    a = a + 1
a = 0
while a < (len(time2)-1):
    b = str(str(time2[a]).split(',')).split('~')
    c = str(str(time2[a+1]).split(',')).split('~')
    d = float(str(b[1]).split(':')[1])
    e = float(str(c[1]).split(':')[1])
    ASS = ASS + (e - d)
    a = a + 1
ASS = round(ASS, 2)
MAXBPM = MAXBPM*bpm
print('-----------------------')
print(f'Natural side:       {NS}')
print(f'Avg Angle Change:   {AAC}')
print(f'Avg Swing Distance: {ASD}')
print(f'Avg Swing Speed:    {ASS}')
print(f'Max BPM:            {MAXBPM}')
print(f'Total RAW:          {ASS+ASD+NS+AAC+MAXBPM}')
print(f'Reccomended CP:     {round((((ASS+ASD+NS+AAC+MAXBPM)/5)/5), 2)}')
