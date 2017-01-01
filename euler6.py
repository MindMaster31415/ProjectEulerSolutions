# "This is my solution for Problem 6 of Project Euler." - Sumedh Garimella
print("Now calculating the difference between the sum of the squares of the first 100 natural numbers and the square of the sum of those numbers...")
i = 0 #starts counter
sum1 = 0 #counter of sum of squares
sum2 = 0 #counter of square of sum
while i <= 100: #when the counter is within the first 100 integers
    sum1 += (i * i) #add the square of the current integer
    sum2 += i #add the integer itself (will square later)
    i += 1 #iterate
sum2 = (sum2 * sum2) #after loop, square the sum
if sum1 > sum2: #which sum is greater?
    print(sum1 - sum2) #we don't want a negative result
else: #if the second sum is greater
    print(sum2 - sum1) #prevents a negative result