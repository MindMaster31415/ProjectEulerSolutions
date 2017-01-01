#This is my solution for Problem 10 of Project Euler." - Sumedh Garimella
print("Now calculating the sum of all primes less than 2 million...")
sum = 0 #counter of sum
i = 2 #first prime number
while i < 2000000: #while the integer we are counting
    for a in range (2, i): #while our factors are less than the integer itself
        if i % a == 0: #if i is divisible by a
            i += 1 #iterate
            break #leaves loop if composite
    else: #if prime
        print(i)
        sum += i #increases sum
        i += 1 #iterate
print(sum) #print result