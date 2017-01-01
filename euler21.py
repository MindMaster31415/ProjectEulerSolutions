# "This is my solution for Problem 21 of Project Euler." - Sumedh Garimella
print("Now calculating the sum of all amicable numbers less than 10000...")
i = 1 #current number being tested
ansum = 0 #sum of all non-perfect amicable numbers
while i < 10000: #while i is less than 10000
    dsum = 0 #d(i)
    s = 0 #d(d(i))
    for a in range(1, i):
        if i % a == 0: #add divisor to dsum if i is divisible by a
            dsum += a
    for b in range(1, dsum): #add divisor to s if dsum is divisible by b
        if dsum % b == 0:
            s += b
    if s == i and i != dsum: #if s is equal to the initial number and the two amicable numbers are not equal to each other (perfect)
        ansum += i #add the number to the total sum (other member of pair is added in a later iteration
        print(i, dsum)
    i += 1 #iterate
print(ansum) #result
