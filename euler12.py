#"This is my solution for Problem 12 of Project Euler." - Sumedh Garimella
print("Now calculating the first triangle number with over 500 divisors...")
i = 1 #first triangular number
t = 0 #count of current triangular number
dmax = 0 #max factors
while dmax < 501:
    t += i
    d = 0
    for a in range(1,t+1):
        if t % a == 0:
            d += 1
    if d > dmax: #checks if there is a new max number of factors
        dmax = d
    i += 1 #iterates
print(t) #displays result