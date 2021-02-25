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
counter = 0
NS = 0
while counter < len(dict0):
    counter2 = 0
    while True:
        try:
            b = str(dict0[f'chunk{counter}'][counter2]).split(',')
            line = str(b[1]).split(':')[1]
            type = str(b[3]).split(':')[1]
            if type == '0':
                if line != '0' or line != '1':
                    NS = NS + 1
            elif type == '1':
                if line != '2' or line != '3':
                    NS = NS + 1
            counter2 = counter2 + 1
        except IndexError:
            counter2 = 0
            break
    counter = counter + 1
counter = 0
while counter < len(dict1):
    counter2 = 0
    while True:
        try:
            b = str(dict1[f'chunk{counter}'][counter2]).split(',')
            line = str(b[1]).split(':')[1]
            type = str(b[3]).split(':')[1]
            if type == '0':
                if line != '0' or line != '1':
                    NS = NS + 1
            elif type == '1':
                if line != '2' or line != '3':
                    NS = NS + 1
            counter2 = counter2 + 1
        except IndexError:
            counter2 = 0
            break
    counter = counter + 1
counter = 0
lines1 = []
cutdir1 = []
time1 = []
MAXBPM = 0
while counter < len(dict0):
    f = len(f'dict0[chunk{counter}]')
    if MAXBPM < f:
        MAXBPM = f
    if dict0[f'chunk{counter}'] != []:
        d = 0
        while True:
            try:
                e = str(dict0[f'chunk{counter}'][d]).split(',')
                f = str(e[0]).split('{')[1]
                lines1.append(f'{counter}~{e[1]}~{e[2]}')
                cutdir1.append(f'{counter}~{e[4]}')
                time1.append(f'{counter}~{f}~{e[3]}')
                d = d + 1
            except IndexError:
                d = 0
                break
    counter = counter + 1
counter = 0
lines2 = []
cutdir2 = []
time2 = []
while counter < len(dict1):
    f = len(f'dict0[chunk{counter}]')
    if MAXBPM < f:
        MAXBPM = f
    if dict1[f'chunk{counter}'] != []:
        d = 0
        while True:
            try:
                e = str(dict0[f'chunk{counter}'][d]).split(',')
                lines2.append(f'{counter}~{e[1]}~{e[2]}')
                cutdir2.append(f'{counter}~{e[4]}')
                f = str(e[0]).split('{')[1]
                time2.append(f'{counter}~{f}~{e[3]}')
                d = d + 1
            except IndexError:
                d = 0
                break
    counter = counter + 1
#Create dict with triangles
counter = 0
b = 0
triangles1 = []
while counter < len(lines1):
    try:
        g = str(lines1[counter]).split('~')
        h = str(lines1[counter+1]).split('~')
        if g[0] == h[0]:
            c = f'{g[1]}~{g[2]}'
            d = f'{h[1]}~{h[2]}'
            f = g[0]
            triangles1.append(f'{f}~{c}~{d}')
    except IndexError:
        break
    counter = counter + 1
    b = b + 2
counter = 0
b = 0
triangles2 = []
while counter < len(lines2):
    try:
        g = str(lines2[counter]).split('~')
        h = str(lines2[counter+1]).split('~')
        if g[0] == h[0]:
            c = f'{g[1]}~{g[2]}'
            d = f'{h[1]}~{h[2]}'
            f = g[0]
            triangles2.append(f'{f}~{c}~{d}')
    except IndexError:
        break
    counter = counter + 1
    b = b + 2
#From the triangle dicts get the lenght between the 2 points and add the Avg Swing Distance points to the point dict
counter = 0
ASD = 0
while counter < len(triangles1):
    try:
        b = str(triangles1[counter]).split('~')
        c = int(str(b[1]).split(':')[1])
        d = int(str(b[2]).split(':')[1])
        e = int(str(b[3]).split(':')[1])
        f = int(str(b[4]).split(':')[1])
        ASD = ASD + getLenght(c, e, d, f)
    except IndexError:
        break
    counter = counter + 1
counter = 0
while counter < len(triangles2):
    try:
        b = str(triangles2[counter]).split('~')
        c = int(str(b[1]).split(':')[1])
        d = int(str(b[2]).split(':')[1])
        e = int(str(b[3]).split(':')[1])
        f = int(str(b[4]).split(':')[1])
        ASD = ASD + getLenght(c, e, d, f)
    except IndexError:
        break
    counter = counter + 1
ASD = round(ASD, 2)
#Get coordiantes of the blocks and put them through the notesToAngle function
counter = 0
AAC = 0
while counter < len(lines1):
    try:
        b = str(lines1[counter]).split('~')
        d = str(b[2]).split(':')
        b = str(b[1]).split(':')
        e = str(lines2[counter]).split('~')
        f = str(e[2]).split(':')
        e = str(e[1]).split(':')
        c = str(str(cutdir1[counter]).split(':')[1]).split('}')
        g = str(str(cutdir2[counter]).split(':')[1]).split('}')
        angle = eval(str(notesToAngle(c[0], int(b[1]), int(d[1]), g[0],int(f[1]), int(e[1]))))*180/math.pi
        AAC = AAC + angle
    except IndexError:
        None
    counter = counter + 1
AAC = round(AAC/(ASD*0.2), 2)
#Get distance between notes per type
counter = 0
ASS = 0
while counter < (len(time1)-1):
    b = str(str(time1[counter]).split(',')).split('~')
    c = str(str(time1[counter+1]).split(',')).split('~')
    d = float(str(b[1]).split(':')[1])
    e = float(str(c[1]).split(':')[1])
    ASS = ASS + (e - d)
    counter = counter + 1
counter = 0
while counter < (len(time2)-1):
    b = str(str(time2[counter]).split(',')).split('~')
    c = str(str(time2[counter+1]).split(',')).split('~')
    d = float(str(b[1]).split(':')[1])
    e = float(str(c[1]).split(':')[1])
    ASS = ASS + (e - d)
    counter = counter + 1
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
