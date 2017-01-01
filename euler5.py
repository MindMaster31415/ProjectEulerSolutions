# "This is my solution for Problem 5 of Project Euler." - Sumedh Garimella
print('Now calculating the smallest integer which can be evenly divided by all integers from 1-20...')
i = 1 #searches for optimal integer
d = 1 #divisor being tested
while d <= 20: #if the condition is yet to be met
    if i % d == 0: #if divisible
        d += 1 #continue
    else: #if not divisible
        d = 1 #restart
        i += 1 #iterate
print(i) #produce final integer
