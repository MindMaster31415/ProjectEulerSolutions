# "This is my solution to Problem 4 of Project Euler." - Sumedh Garimella
print("Now finding the largest palindrome product of two 3-digit integers...")
a = 100  # smallest 3-digit integer
b = 100  # smallest 3-digit integer
lim = 1000  # a and b must be less than this integer
pmax = 0  # keeps track of biggest palindrome under set conditions
while (a < lim):  # when a is a 3 digit integer
    while (b < lim):  # when b is a 3 digit integer
        prod = str(a * b)  # converts the product into a string to check for palindromes
        n = len(prod)  # length of the product integer
        if (prod[0] == prod[n - 1]) and (prod[1] == prod[n - 2]) and (prod[2] == prod[n - 3]) and (a * b > pmax):  # checks for a palindrome
            pmax = a * b  # biggest palindrome
        b += 1  # iteration
    a += 1  # iteration
    b = 100  # resets the counter for b
print(pmax)