from functionlib import *

print('--------------')
 
#Takes the inputs.
score = int(input('Score: ')) 
mods = input('modifiers: ').split(', ')
notes = int(input('notes: '))
weight = float(input('weight: '))

pog = modToRaw(score, mods) #Takes your score and removes any modifiers.
acc = scoreToAcc(notes, pog) #Takes score and puts it into a accuracy percentage (can be > 100).
cp = getScore(0, acc, weight) # Takes score and calculates your CP (points).


print('--------------') 
print(f'acc = {acc}') #Tells you your accuracy.
print(f'cp = {cp}') #Tells you your CP.
