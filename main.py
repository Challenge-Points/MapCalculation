from functionlib import *

print('--------------')

score = int(input('Score: '))
mods = input('modifiers: ').split(', ')
notes = int(input('notes: '))
weight = float(input('weight: '))

pog = modToRaw(score, mods)
acc = scoreToAcc(notes, pog)
cp = getScore(0, acc, weight)

print('--------------')
print(f'acc = {acc}')
print(f'cp = {cp}')