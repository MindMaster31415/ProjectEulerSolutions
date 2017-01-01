# "This is my solution for Problem 16 of Project Euler." - Sumedh Garimella
print("Now calculating the sum of the digits of 2^1000...")
i = 1 #counter of exponent
n = 1 #number
while i <= 1000: #while exponent is no greater than 1000
    n = n * 2 #multiply by 2
    i += 1
a = str(n) #allows to extract all digits of n
x = len(a) #for our loop
z = 0 #counter for the upcoming loop
sum = 0 #counter for sum
while z < x: #while we are still within the length of a
    sum += int(a[z]) #add the digit value to the sum
print(sum) #result
