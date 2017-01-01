#This is my solution for Problem 15 of Project Euler." - Sumedh Garimella
#source - http://blog.dreamshire.com/project-euler-15-solution/ (just equation, no code copied)
print("Now calculating the number of paths in a 20x20 lattice grid...")
d = 20 #amount of downward moves
r = 20 #amount of rightward moves
nf = 1 #numerator factorial (40!)
df = 1 #downward factorial (20!)
rf = 1 #rightward factorial (20!)
i = 1 #start counter
while i <= 40:
    nf = nf * i #keep multiplying
    i += 1 #iterate
i = 1 #restart
while i <= 20:
    df = df * i #downward
    rf = rf * i #rightward
    i += 1 #iterate
c = nf / (df * rf) #equation
print(c) #result