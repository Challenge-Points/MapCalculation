# Map Calculation

Challenge Ranking System for Beat Saber

# How do we calculate the wight of a map?

these are the criteria we set for a map

-   Notes on natural side
-   Avg angle Change
-   Avg swing distance
-   Avg swing speed

i'll explain all of them in depth later, but before that there is some basic knowledge you should have before reading any of this
So the map is devided into chunks and those chunks give point values which later get added up into a final point level, which is the weight of the map. each chunk is 2 beats long, the program runs twice, 1 time starting from beat 0 and 1 time starting from beat 1 to avoid severe angle changes between the first chunks not being counted for in the final cp value.

## Notes on the natural side

If you watched or played any beat saber you know that blue is on the right and red is on the left, but some maps like to switch this a round sometimes, which should lead to an increase of score.

#### Points = The amount of notes that arent on the natural side

## Avg angle change

This one is a bit more difficult, so bare with me here, so basically what it does is it draws 2 lines through each note, then when the lines hit (if they hit, more on this later) it takes 2 angles, left angle and the right angle, then the smallest of these 2 angles is the amount of points one gets.

#### Points = The angle change in degrees/(ASD\*0.1)

## Avg swing distance

This one is also a selfexplenatory one, it takes the avg distance between the notes.

#### Points = The distance between the notes

## Avg swing speed

The avarage speed someone has to swing at per chunk

#### Points = The Distance between 2 notes\*10

## Total

There are 2 values we get at the end, the Total RAW value and the Total value, the total raw value is all the points added up normally, and the Total value is the Total RAW value divided by 20
