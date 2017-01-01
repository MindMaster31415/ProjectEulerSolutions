# "This is my solution for Problem 3 of Project Euler." - Sumedh Garimella
print("Now calculating the prime factors of the number 600851475143...")
n = 600851475143 #our integer
c = 2 #first possible prime factor
pfactors = [] #running count of all prime factors
while (c <= n): #while our prime factor is less than the integer we are trying to get the prime factors of
    if (n % c == 0): #if our number is divisible
        n = n / c #continues the division process
        print(c) #displays the prime factor
        pfactors.append(c) #continues our list
        c -= 1 #turns the iterator backwards to allow for multiple divisions of the same prime factor
    c += 1 #iteration
