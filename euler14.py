#"This is my solution for Problem 14 of Project Euler." - Sumedh Garimella
print("Now printing the number under 1 million which creates the longest Collatz Sequence...")
i = 1 #count of the number being counted
d = 1 #length of Collatz Sequence
imax = 0 #number which creates longest collatz sequence
dmax = 1 #length of given sequence (since 1 or the first number itself is a step, we count it automatically
while i < 1000000: #while the number being counted is less than 1 million
    n = i #n is a number we can execute operations on without altering the iteration
    while n > 1: #ends on 1
        if n % 2 == 0: #if even
            n = n/2
        else: #if odd
            n = 3*n + 1
        d += 1 #iterate
    if d > dmax: #if greater than maximum
        dmax = d
        imax = i
    i += 1 #iterate
    d = 1
print("Result: ", imax, dmax) #result
