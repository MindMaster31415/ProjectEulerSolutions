#"This is my solution for Problem 7 of Project Euler." - Sumedh Garimella
#reference: Stack Overflow - http://stackoverflow.com/questions/18833759/python-prime-number-checker
print("Now calculating the 10,001st prime number...")
p = 10001 #how many primes we will be counting
i = 2 #first factor tested must be greater than 1
while p > 0: #while we are still counting
    for a in range(2,i): #while the factor tested is less than the actual integer
        if i % a == 0: #if i is divisible by a
            i += 1 #iterates
            break #restarts the loop with the next integer
    else: #if there is no non-1 and non-i factor of i
        p -= 1 #one more prime found
        print(i) #displays prime number
        i += 1 #iterates
i -= 1 #since the final count will be one greater than the actual prime we are looking for, we need to switch back
print("The 10,001st prime is:", i) #result!
