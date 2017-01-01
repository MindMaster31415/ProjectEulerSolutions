#"This is my solution for Problem 9 of Project Euler." - Sumedh Garimella
print("Now calculating the product abc for the Pythagorean triplet for which a + b + c = 1000...")
a = 1 #initial
b = 1
c = 1
while a <= 500: #these are in place to allow for an optimized search for the correct pythagorean triplet
    while b <= 500:
        while c <= 500:
            if (a*a + b*b == c*c): #checks if pythagorean triplet exists
                if (a + b + c == 1000): #is the sum of the triplet equal to 1000?
                    print(a, b, c)
                    print(a*b*c)
            c += 1 #iterations to keep cycle going
        b += 1
        c = 1
    a += 1
    b = 1
    c = 1
