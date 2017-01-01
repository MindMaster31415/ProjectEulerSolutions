#"This is my solution for Problem 25 of Project Euler." - Sumedh Garimella
print("Now calculating the index of the first Fibonacci term with 1000 digits...")
a,b = 1,1 #start of Fibonacci sequence
bindex = 1 #index of the fibonacci number being counted
dmax = 0 #max digits in any Fibonacci term
while (dmax < 1000): #while we are still not at 1000 digits for any term
    d = len(str(b)) #amount of digits in the term
    if d > dmax: #if we have a new max
        dmax = d
    temp = a #allows for new top two Fibonacci terms
    a = b
    b += temp
    bindex += 1 #our index increases by 1
print(bindex, b) #result
