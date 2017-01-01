#"This is my solution for Problem 20 of Project Euler." - Sumedh Garimella
print("Now calculating the sum of all digits in 100 factorial...")
i = 1 #counts the current number being multiplied to n
n = 1 #factorial value for i as it increases
while i <= 100: #while we are still counting a number no greater than 100
    n = n * i #multiply current value by i
    i += 1 #iterate
print(n)
f = str(n) #convert to string to add each digit to the final sum
s = 0 #sum
x = 0 #counter of digits added to the sum
while x < len(f): #while not all digits have been counted
    s += int(f[x]) #add value of current digit to the sum
    x += 1 #iterate
print("The sum is: ", s) #result