# Majora's Mask Title Theme Song

Clock.bpm=150
Scale.default=("major")
Root.default.set(2)

#Intro
#m0 >> viola([(0,4,7),(-1,4,6),(-2,3,5),(-1,4,6)],dur=[3,3,3,3],amplify=0.3,oct=4,delay=-0.22)
#2nd ending
#m1 >> viola([(0,4,7),(-1,4,6),(-2,3,5),(-1,4,6),(0,4,7)],dur=[3,3,3/2,3/2,3],amplify=0.3,oct=4,delay=-0.22)
m3 >> viola([(0,4,7),(-1,4,6),(-2,3,5),(-1,4,6),(0,4,7),(-1,4,6),(-2,3,5),(-1,4,6),(0,4,7)],dur=[3,3,3,3,3,3,3/2,3/2,3],amplify=0.3,oct=4,delay=-0.22)

# Main melody
#m1 >> pluck([0,7,6,5,4,5,3],dur=P[2,1,1,1,1,3,3]/2,amplify=0.2,oct=5)
#m1 >> pluck([4,1,4,3,1,3,4,2],dur=P[2,1,1,1,1,2,1,3]/2,amplify=0.2,oct=5)
#m1 >> pluck([0,7,6,5,4,5,3],dur=P[2,1,1,1,1,3,3]/2,amplify=0.2,oct=5)
#m1 >> pluck([4,3,1,3,2,0],dur=P[1,1,1,2,1,6]/2,amplify=0.2,oct=5)
m1 >> pluck([0,7,6,5,4,5,3,4,1,4,3,1,3,4,2,0,7,6,5,4,5,3,4,3,1,3,2,0],dur=P[2,1,1,1,1,3,3,2,1,1,1,1,2,1,3,2,1,1,1,1,3,3,1,1,1,2,1,6]/2,amplify=0.5,oct=5)

# 1st Flute sound (substitute synthdef)
m2 >> bell([4,7,6,5,4,7,8,6,7],dur=[3,3,3,3,3,3,3/2,3/2,3],amplify=0.15,oct=6)



# strings
t0 >> saw([2,2,4,7,4,2],dur=[1],amplify=0.3,oct=5)

t0 >> saw([3,4,3,6,4,3],dur=[1],amplify=0.3,oct=5)

t0 >> saw([6,4,3],dur=[4],amplify=0.3,oct=5)

# 2nd melody
m4 >> sitar([0,0,0,-1,0,1,-3,3,2,3,2,0,1,-3,0,0,0,-1,0,1,-3,3,2,3,2,-1,0],dur=P[2,1,1,1,1,3,3,1,1,1,2,1,3,3,2,1,1,1,1,3,3,1,1,1,2,1,6]/2,amplify=0.4,oct=6)

# 2nd Flute solo
m2 >> bell([0,3,2,1,0,3,4,2,3],dur=[3,3,3,3,3,3,3/2,3/2,3],amplify=0.15,oct=6)


t0 >> saw([0],amplify=0.3)
