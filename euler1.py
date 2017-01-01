#"This is my solution for Problem 1 of Project Euler." - Sumedh Garimella
print("Now calculating the sum of all multiples of 3 and 5 below 1000...")
mult_sum = 0 #keeps track of the sum of all counted multiples
count = 0 #current number being tested

while count < 1000: #for all nonnegative integers less than 1000,
    if (count % 3 == 0 or count % 5 == 0): #if this number is a multiple of either 3 or 5
    	mult_sum += count #add this to the rolling sum
    count += 1 #iterator
print(mult_sum)  #after all possible numbers are counted, this gives the final sum
