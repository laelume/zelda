# 2. Bolero of Fire

Clock.bpm=230
Scale.default=("minor")
Root.default.set(0)
#b0 >> soprano(P[6,4,6,4,8,6,8,6],dur=P[1,1,1,1,1,1,1,5],amplify=0.5,oct=5)
#b1 >> soprano(P[7,5.5,7,5.5,9,7,9,7],dur=P[1,1,1,1,1,1,1,5],amplify=0.5,oct=5)
#b2 >> soprano(P[8,6,8,6,11,8,11,8,13,11,13,11,15,12.5,15,12.5],dur=P[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],amplify=0.5,oct=5)
#b3 >> soprano(P[14,10.5,14,10.5,13,11.5,8,6,4],dur=P[1,1,1,1,1,1,1,1,16],amplify=0.5,oct=5)
bx >> soprano(
P[6,4,6,4,8,6,8,6,6,4,6,4,8,6,8,6,7,5.5,7,5.5,9,7,9,7,8,6,8,6,11,8,11,8,13,11,13,11,15,12.5,15,12.5,14,10.5,14,10.5,13,11.5,8,6,4],dur=P[1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8],amplify=0.5,oct=5)

# OR, e.g., shifting to a different tonic
#Scale.default=("major")
#Root.default.set(5)
#bx >> soprano(P[3,1,3,1,5,3,5,3] ,dur=P[1],amplify=0.5,oct=5)