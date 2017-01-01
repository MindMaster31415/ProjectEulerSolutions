#"This is my solution for Problem 2 of Project Euler." - Sumedh Garimella
print("Now calculating the sum of all even Fibonacci numbers less than 4 million...")
a,b = 1,2 #initial Fibonacci numbers, a and b represent the two most recent numbers
sum = 0 #keeps track of rolling sum
while (b < 4000000): #we are only counting Fibonacci numbers less than 4 million
    if (b%2 == 0): #only if this number is even
        sum += b #value of even Fibonacci number is counted
    temp = a #placeholder for original
    a = b #makes room for the next number
    b += temp #creates new Fibonacci number
print(sum) #after b reaches 4 million, this prints the sum
